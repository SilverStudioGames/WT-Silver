init python:
    class Doll(DollMethods):
        def __init__(self, name, clothes, face, body):
            self.wardrobe = {}
            self.wardrobe_list = []
            self.blacklist = []
            self.outfits = []
            self.name = name
            self.clothes = clothes
            self.face = DollFace(self, face)
            self.body = DollBody(self, body)
            self.cum = DollCum(self)
            self.pose = None

            self.rebuild_image()

        def rebuild(self):
            """Rebuild all character images. Useful for debugging."""
            self.body.rebuild_image()
            self.face.rebuild_image()
            self.cum.rebuild_image()
            for o in self.wardrobe_list:
                o.rebuild_image()
                o.build_icon()
            for o in self.outfits:
                o.rebuild_image()
            self.rebuild_image()

        def build_image(self):
            # Add body, face, cum, clothes, masks
            masks = []
            sprites = [[self.body.get_image(), 0], [self.face.get_image(), 1], [self.cum.get_image(), self.cum.zorder_cum]]

            for o in self.clothes.itervalues():
                if o[0] and o[2]:
                    zorder = o[0].zorder

                    sprites.append([o[0].get_image(), zorder])

                    if o[0].back:
                        sprites.append([o[0].get_back(), -100+zorder])

                    if o[0].front:
                        sprites.append([o[0].get_front(), 100+zorder])

                    if o[0].armfix:
                        sprites.append([o[0].get_armfix(), zorder+0.5])

                    if o[0].mask:
                        masks.append([o[0].mask, zorder-1])

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
            return tuple(x[0] for x in sprites)

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

        def apply_transition(self):
            if not renpy.is_skipping():
                scr_name = "{}_main".format(self.name)
                if renpy.get_screen(scr_name):
                    renpy.hide_screen(scr_name)
                    renpy.show_screen(scr_name)
                else:
                    last_doll_images[scr_name] = self.get_image()

        def equip(self, obj):
            """Takes DollCloth or DollOutfit object to equip."""
            if isinstance(obj, DollCloth):
                self.clothes[obj.type][0] = obj
                self.clothes[obj.type][2] = True

                if self.is_blacklisted(obj.type):
                    self.unequip(*self.get_blacklister(obj.type))

                if obj.blacklist:
                    self.unequip(*obj.blacklist)

                if self.pose:
                    obj.set_pose(self.pose)
            elif isinstance(obj, DollOutfit):
                self.unequip("all")
                for i in obj.group:
                    self.clothes[i.type][0] = i.parent
                    self.clothes[i.type][0].set_color(i.color)
                    if self.pose:
                        i.parent.set_pose(self.pose)
            self.body.rebuild_image()
            self.rebuild_image()
            self.rebuild_blacklist()
            self.apply_transition()
            update_chibi(self.name)

        def unequip(self, *args):
            """Takes argument(s) containing string cloth type(s) to unequip."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k in self.blacklist_unequip:
                        if self.pose:
                            v[0].set_pose(None)
                        v[0], v[2] = None, True
            else:
                for arg in args:
                    if not arg in self.blacklist_unequip:
                        if self.pose and self.clothes[arg][0]:
                            self.clothes[arg][0].set_pose(None)
                        self.clothes[arg][0] = None

            self.body.rebuild_image()
            self.rebuild_image()
            self.rebuild_blacklist()
            self.apply_transition()
            update_chibi(self.name)

        def get_equipped(self, type):
            """Takes argument containing string cloth type. Returns equipped object for cloth type."""
            return self.clothes[type][0]

        def get_equipped_item(self, items):
            """Returns first equipped item from a list or None."""
            for i in items:
                if self.is_equipped_item(i):
                    return i
            return None

        def strip(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        v[2] = False
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = False
                    else:
                        self.clothes[arg][2] = False
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def wear(self, *args):
            """Takes argument(s) containing string cloth type(s) to put on (unhide)."""
            if "all" in args:
                if self.is_worn("all"):
                    return

                for v in self.clothes.itervalues():
                    v[2] = True
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = True
                    else:
                        self.clothes[arg][2] = True
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def toggle_wear(self, type):
            """Takes argument containing string cloth type to toggle visibility (hide/unhide). Used in wardrobe."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type):
                        v[2] = not v[2]
            else:
                self.clothes[type][2] = not self.clothes[type][2]
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()
            update_chibi(self.name)

        def is_equipped(self, type):
            """Takes argument containing string cloth type. Returns True if slot is occupied, False otherwise."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type) and v[0]:
                        return True
                return False
            else:
                return True if self.clothes[type][0] else False

        def is_equipped_item(self, item):
            """Takes DollCloth object or list of objects. Returns True if item is equipped, False otherwise."""
            return self.get_equipped(item.type) == item

        def is_worn(self, *args):
            """Takes argument(s) containing string cloth type(s). Returns True if worn, False otherwise."""
            if "all" in args:
                for v in self.clothes.itervalues():
                    if not v[2]:
                        return False
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k, v in self.clothes.iteritems():
                            if k.startswith(arg) and not v[0] or not v[2]:
                                return False
                    else:
                        if not self.clothes[arg][0] or not self.clothes[arg][2]:
                            return False
            return True

        def is_any_worn(self, *args):
            """Takes arguments containing string cloth types. Returns True if ANY of them is worn, False otherwise."""
            if "clothes" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        if self.is_worn(k):
                            return True
            else:
                for arg in args:
                    if self.is_worn(arg):
                        return True
            return False

        def set_face(self, **kwargs):
            """Takes keyword argument(s) with the string name of expression file(s)."""
            if self.face.set_face(**kwargs):
                self.body.rebuild_image()

                # Rebuild lipstick
                lipstick = self.clothes.get("makeup4", [None, 1, True])[0]
                if isinstance(lipstick, DollLipstick):
                    lipstick.rebuild_image()
                self.rebuild_image()

        def set_face_zorder(self, **kwargs):
            """Takes keyword argument(s) with the name(s) of body part(s) and integer value(s)"""
            if self.face.set_zorder(**kwargs):
                self.rebuild_image()

        def get_face(self):
            """Returns a dictionary containing currently set facial expressions. Used in character studio."""
            return self.face.get_face()

        def set_body(self, **kwargs):
            """Takes keyword argument(s) with the string name of body part file(s)."""
            if self.body.set_body(**kwargs):
                self.rebuild_image()

        def set_body_hue(self, arg):
            """Takes integer between 0 - 359, rotates the character body colour by given amount."""
            self.body.hue = arg
            self.body.rebuild_image()
            self.rebuild_image()
            self.apply_transition()

        def set_body_zorder(self, **kwargs):
            """Takes keyword argument(s) with the name(s) of body part(s) and integer value(s)"""
            if self.body.set_zorder(**kwargs):
                self.rebuild_image()

        def set_cum(self, *args, **kwargs):
            """Takes keyword argument(s) containing string name(s) of cum layers to apply or None."""
            if self.cum.set_cum(*args, **kwargs):
                self.body.rebuild_image()
                self.rebuild_image()
                self.apply_transition()

        def set_pose(self, pose):
            if pose is None or renpy.loadable("characters/{}/poses/{}/loadable.webp".format(self.name, pose)):
                self.pose = pose
                self.face.set_pose(pose)
                self.body.set_pose(pose)
                self.cum.set_pose(pose)
                for v in self.clothes.itervalues():
                    if v[0]:
                        v[0].set_pose(pose)
                self.rebuild_image()
                self.apply_transition()
            else:
                raise Exception("'{}' pose doesn't exist for character named '{}'.".format(pose, self.name))

        def rebuild_blacklist(self):
            blacklist = []
            for v in self.clothes.itervalues():
                if v[0]:
                    blacklist.extend(v[0].blacklist)
            self.blacklist = list(set(blacklist))

        def is_blacklisted(self, type):
            """Takes string cloth type. Returns True if cloth type is blacklisted."""
            return True if type in self.blacklist else False

        def get_blacklister(self, type):
            """Takes string cloth type. Returns a list of clothing types that report incompatibility."""
            return [x[0].type for x in self.clothes.itervalues() if x[0] and type in x[0].blacklist]

        def create_outfit(self):
            """Creates a copy of the current character clothes and stores it."""
            return DollOutfit([x[0] for x in self.clothes.itervalues() if x[0]], True)

        def import_outfit(self, path, fromfile=True):
            """Imports outfit from .png file or clipboard text."""
            # Grab data
            if fromfile:
                try:
                    imported = image_payload.decode(path)
                except:
                    if image_payload._file:
                        image_payload._file.close()
                    renpy.notify("Import failed: Corrupted file.")
                    return None
            else:
                imported = get_clipboard()

            # Evaluate data
            if imported:
                try:
                    imported = make_revertable(evaluate(imported))
                except:
                    renpy.notify("Import failed: Corrupted outfit data.")
                    renpy.block_rollback()
                    return None

                group = []

                for i, x in enumerate(imported):
                    if i == 0 and not x == self.name:
                        renpy.notify("Import failed: Wrong character.")
                        return None

                    for o in self.wardrobe_list:
                        if x[0] == o.id:
                            if not o.unlocked and not game.cheats:
                                renpy.notify("Import failed: You don't own these items. Buy them first.")
                                return None

                            x[0] = o.clone()
                            x[0].set_color(x[1])
                            group.append(x[0])

                if group:
                    renpy.notify("Import successful!")
                    return DollOutfit(group, True)
            renpy.notify("Import failed: Unknown error.")
            return None

        def get_schedule(self):
            """Returns a list of outfits available for current time of day and weather conditions."""
            schedule = []

            for o in self.outfits:
                if o.unlocked and o.schedule["day" if game.daytime else "night"]:
                    if weather == "overcast" and o.schedule["cloudy"]:
                        schedule.append(o)
                    elif weather in {"storm", "rain"} and o.schedule["rainy"]:
                        schedule.append(o)
                    elif weather in {"snow", "blizzard"} and o.schedule["snowy"]:
                        schedule.append(o)
                    elif weather in {"clear", "cloudy"} and not (o.schedule["cloudy"] or o.schedule["rainy"] or o.schedule["snowy"]):
                        schedule.append(o)
            return schedule

        def equip_random_outfit(self):
            """Equips random outfit based on Outfits Schedule."""
            schedule = self.get_schedule()

            if schedule:
                self.equip(renpy.random.choice(schedule))
