init python:
    class DollOutfit(DollMethods):
        def __init__(self, group, unlocked=False, name="", desc="", price=0):
            self.name = name
            self.group = [x.clone() if not x.parent else x for x in group]
            self.desc = desc
            self.price = price
            self.char = self.group[0].char
            self.unlocked = unlocked
            self.schedule = {"day": False, "night": False, "cloudy": False, "rainy": False, "snowy": False}
            self.hash = self.generate_hash()

            if unlocked:
                self.unlock()

            # Append to character outfits list
            self.char.outfits.append(self)

            self.rebuild_image()

        def __del__(self):
            print("Outfit with hash: {} has been garbage collected.".format(self.hash))

        def delete(self):
            if self in self.char.outfits:
                self.char.outfits.remove(self)
            del self

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

            sprites.sort(key=lambda x: x[1])

            back_sprites = [x for x in sprites if x[1] < 0]
            sprites = [x for x in sprites if x[1] >= 0]

            # Apply alpha mask
            for m in sorted(masks, key=lambda x: x[1]):
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

        def generate_hash(self):
            salt = str( [(x.name, x.type, x.id, x.color) for x in self.group] )
            return hash(salt)

        def validate(self):
            for i in self.char.outfits:
                if i.unlocked and not i == self and i.hash == self.hash:
                    return False
            return True

        def export_data(self, tofile=True, filename="exported"):
            """Exports outfit to .png file or clipboard text."""
            exported = [self.group[0].name]
            exported.extend([x.id, x.color] for x in self.group)

            # Encode data
            if tofile:
                path = "{}/game/outfits/".format(config.basedir)
                fn = "{}.png".format(filename)

                if not os.path.exists(path):
                    os.makedirs(path)

                path = path+fn
                renpy.screenshot(path)
                img = pygame.image.load(path)
                img = pygame.transform.smoothscale(img, (1080, 600))
                subsurface = img.subsurface((384, 63, 309, 470))
                pygame.image.save(subsurface, path)
                image_payload.encode(filename, str(exported))
            else:
                set_clipboard(exported)
            renpy.notify("Export successful!")

        def import_data(self, fromfile=True, filename="exported"):
            """Imports outfit from .png file or clipboard text."""
            # Grab data
            if fromfile:
                try:
                    if renpy.loadable("/outfits/{}.png".format(filename)):
                        imported = image_payload.decode(filename)
                    else:
                        renpy.notify("File doesn't exist!")
                        return False
                except:
                    if image_payload._file:
                        image_payload._file.close()
                    renpy.notify("Corrupted file!")
                    return False
            else:
                imported = get_clipboard()

            # Evaluate data
            if imported:
                try:
                    imported = make_revertable(evaluate(imported))
                except:
                    renpy.notify("Corrupted file!")
                    renpy.block_rollback()
                    return False

                group = []

                for x in imported:
                    if isinstance(x, list):
                        for o in char_active.wardrobe_list:
                            if x[0] == o.id:
                                if not o.unlocked and not cheats_active:
                                    renpy.notify("You haven't unlocked some of the items yet. Try again later.")
                                    return False
                                x[0] = o.clone()
                                x[0].set_color(x[1])
                                group.append(x[0])
                if len(group) > 0:
                    renpy.notify("Import successful!")
                    return DollOutfit(group, True)
            renpy.notify("Import failed!")
            return False

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
