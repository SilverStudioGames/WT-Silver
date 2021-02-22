init python:
    class DollOutfit(DollMethods):
        default_schedule = {"day": False, "night": False, "cloudy": False, "rainy": False, "snowy": False}

        def __init__(self, group, unlocked=False, name="", desc="", price=0, temp=False, schedule={}, hidden=False):
            self.group = [x.clone() if not x.parent else x for x in group]
            self.name = name
            self.desc = desc
            self.price = price
            self.char = self.group[0].char
            self.unlocked = unlocked
            self.schedule = dict(self.default_schedule.items() + schedule.items())
            self.hash = self.generate_hash()
            self.temp = temp
            self.hidden = hidden

            if not self.temp:

                if unlocked:
                    self.unlock()

                if not self.hidden and not self in self.char.outfits:
                    self.char.outfits.append(self)

                self.rebuild_image()

        if config.developer:
            def __del__(self):
                print("Outfit with hash: {} has been garbage collected.".format(self.hash))

        def __eq__(self, obj):
            if not isinstance(obj, DollOutfit):
                return NotImplemented
            return self.hash == obj.hash

        def generate_hash(self):
            salt = str( sorted([ sorted([x.name, x.type, x.id, x.color]) for x in self.group ]) )
            return hash(salt)

        def delete(self):
            if self in self.char.outfits:
                self.char.outfits.remove(self)

        def build_image(self):
            masks = []
            sprites = []

            # Add body parts and skin layers from clothes, then make them grayscale
            sprites.append([self.char.body.get_mannequin(self.group), 0])

            for o in self.group:
                sprites.append([o.get_image(), o.zorder])

                if o.back:
                        sprites.append([o.get_back(), -100+o.zorder])

                if o.front:
                    sprites.append([o.get_front(), 100+o.zorder])

                if o.armfix:
                    sprites.extend([[gray_tint("{}armleft/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armleft"))), o.zorder+0.5], [gray_tint("{}armright/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armright"))), o.zorder+0.5]])

                if o.mask:
                    masks.append([o.mask, o.zorder-1])

            sprites.sort(key=itemgetter(1))

            back_sprites = [x for x in sprites if x[1] < 0]
            sprites = [x for x in sprites if x[1] >= 0]

            # Apply alpha mask
            for m in sorted(masks, key=itemgetter(1)):
                for i, s in enumerate(sprites):
                    if m[1] <= s[1]:
                        if i > 0:
                            masked = tuple(x[0] for x in sprites[:i])
                            c = AlphaMask(Fixed(*masked, fit_first=True), m[0])
                            sprites = sprites[i:]
                            sprites.insert(0, (c, m[1]-1))
                        break

            sprites = back_sprites + sprites
            sprites = tuple(x[0] for x in sprites)
            return sprites

        def get_image(self):
            if not renpy.is_skipping() or self.sprite is None:
                if self.override:
                    sprites = self.build_image()
                    self.sprite = DollDisplayable(Fixed(*sprites, fit_first=True))
                elif not self.cached:
                    sprites = self.build_image()
                    self.sprite = DollDisplayable(Fixed(*sprites, fit_first=True))
                    self.cached = True
            return self.sprite

        def exists(self):
            return (self in self.char.outfits)

        def export_data(self, filename, tofile=True):
            """Exports outfit to .png file or clipboard text."""
            exported = [self.group[0].name]
            exported.extend([x.id, x.color] for x in self.group)

            # Encode data
            if tofile:
                path = "{}/game/outfits/".format(config.basedir)
                fn = "{}.png".format(filename)

                if not os.path.exists(path):
                    os.makedirs(path)

                d = Transform(self.get_image(), crop=(210, 200, 700, 1000), anchor=(0.5, 1.0), align=(0.5, 1.0), xsize=310, ysize=470, fit="contain")
                d = Fixed(
                    "interface/wardrobe/export_background.webp",
                    d,
                    "interface/wardrobe/export_frame.webp",
                    Text(active_girl, align=(0.5, 0.995)),
                    Text("Ver. {}".format(config.version), size=10, align=(0.99, 0.99))
                )

                displayable_to_file(d, path+fn, size=(310, 470) )
                image_payload.encode(filename, str(exported))
            else:
                set_clipboard(exported)
            renpy.notify("Export successful!")

        def unlock(self):
            """Unlocks outfit and respective clothing objects from which they were cloned."""
            self.unlocked = True
            for i in self.group:
                i.unlocked, i.parent.unlocked = True, True

        def save(self):
            """Overwrites this outfit with clothes currently equipped by the character."""
            self.group = []
            for v in self.char.clothes.itervalues():
                if v[0]:
                    self.group.append(v[0].clone())
            self.rebuild_image()
            return

        def is_modded(self):
            """Returns True if one of the group items comes from a mod."""
            for i in self.group:
                if i.is_modded():
                    return True
            return False

        def get_modname(self):
            """Returns a list of mods contained within the outfit group."""
            return list(set([i.get_modname() for i in self.group if i.is_modded()]))

        def get_schedule(self):
            """Returns a dictionary with the current schedule."""
            return self.schedule

        def set_schedule(self, **kwargs):
            for k, v in kwargs.iteritems():
                self.schedule[k] = v
