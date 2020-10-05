init python:
    class DollCloth(DollMethods):
        def __init__(self, name, categories, type, id, color, zorder=None, unlocked=False, level=0, blacklist=None, parent=None, armfix=False, modpath=""):
            self.name = name
            self.char = eval(name)
            self.categories = categories
            self.type = type
            self.id = id
            self.color = color
            self.color_default = [x[:] for x in color]
            self.unlocked = unlocked
            self.layers = len(color)
            self.parent = parent
            self.ico = None
            self.blacklist = blacklist
            self.level = level
            self.modpath = modpath
            self.armfix = armfix
            self.back_outline = None
            self.front_outline = None

            # Inherit zorder from character if needed
            self.zorder = zorder if zorder else self.char.clothes[type][1]

            self.set_imagepath()
            self.set_layers()

            # Add to character wardrobe and unordered list
            if not parent:
                self.char.wardrobe.setdefault(self.categories[0], {}).setdefault(self.categories[1], []).append(self)
                self.char.wardrobe_list.append(self)

            self.rebuild_image()

        def set_imagepath(self):
            if any(x in self.type for x in ("makeup", "accessory", "piercing", "tattoo")):
                subpath = self.type[:-1]
            else:
                subpath = self.type

            path = "{}/characters/{}/clothes/{}/{}/".format(self.modpath, self.name, subpath, self.id)

            if renpy.loadable(path + "0.webp"):
                self.imagepath = path
                return
            raise IOError("Couldn't find file \"{}/characters/{}/clothes/{}/{}/0.webp\"".format(self.modpath, self.name, subpath, self.id))

        def set_layers(self):
            for x in self.layers_special:
                path = "{}{}.webp".format(self.imagepath, x)
                self.__dict__[x] = path if renpy.loadable(path) else None

            for x in self.layers_additional:
                self.__dict__[x] = []
                for i in xrange(self.layers):
                    path = "{}{}_{}.webp".format(self.imagepath, i, x)
                    if renpy.loadable(path):
                        self.__dict__[x].append(path)
                if self.__dict__[x]:
                    path = "{}outline_{}.webp".format(self.imagepath, x)
                    self.__dict__[x+"_outline"] = path if renpy.loadable(path) else None

        def build_image(self):
            sprites = []

            # Add colorable layers and color them
            sprites.extend((self.apply_color("{}{}.webp".format(self.imagepath, x), x), x) for x in xrange(self.layers))

            # Add extra layers if exist
            for n, x in enumerate(self.layers_extra):
                path = "{}{}.webp".format(self.imagepath, x)
                if renpy.loadable(path):
                    sprites.append((path, self.layers+n))

            sprites.sort(key=itemgetter(1))
            sprites = tuple(x[0] for x in sprites)
            return sprites

        def build_icon(self):
            sprites = [
                [self.get_back(), -100+self.zorder],
                [self.char.body.get_mannequin([self]), 0],
                [self.get_front(), 100+self.zorder],
                [self.get_image(), self.zorder]
            ]

            if self.armfix:
                sprites.append([self.get_armfix(mannequin=True), self.zorder+0.5])

            bounds = "{}outline.webp".format(self.imagepath) if renpy.loadable("{}outline.webp".format(self.imagepath)) else "{}0.webp".format(self.imagepath)

            sprites.sort(key=itemgetter(1))
            sprites = tuple(x[0] for x in sprites)
            return (sprites, bounds)

        def get_back(self):
            """Returns a list of layers displayed in the back of object/character"""
            back_outline = [self.back_outline] if self.back_outline else []
            sprites = [self.apply_color(x, n) for n, x in enumerate(self.back)] + back_outline
            return Fixed(*sprites, fit_first=True)

        def get_front(self):
            """Returns a list of layers displayed in the front of object/character"""
            front_outline = [self.front_outline] if self.front_outline else []
            sprites = [self.apply_color(x, n) for n, x in enumerate(self.front)] + front_outline
            return Fixed(*sprites, fit_first=True)

        def get_armfix(self, mannequin=False):
            if mannequin:
                armleft = gray_tint("{}armleft/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armleft")))
                armright = gray_tint("{}armright/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armright")))
            else:
                armleft = Transform("{}armleft/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armleft")), matrixcolor=HueMatrix(self.char.body.hue))
                armright = Transform("{}armright/{}_fix.webp".format(self.char.body.imagepath, self.char.body.get_part("armright")), matrixcolor=HueMatrix(self.char.body.hue))
            return Fixed(armleft, armright, fit_first=True)

        def get_icon(self):
            """Returns cropped Fixed displayable"""
            if not renpy.is_skipping() or self.ico is None:
                sprites, bounds = self.build_icon()
                self.ico = CroppedImage(sprites, bounds).get_image()
            return self.ico

        def apply_color(self, img, n):
            """Takes image and int layer number. Used internally."""
            c = TintMatrix(tuple(self.color[n]))
            return Transform(img, matrixcolor=c)

        def set_color(self, n):
            """Takes int layer number for manual color picking or a list to replace the cloth color in its entirety."""
            if isinstance(n, int):
                self.char.override, self.override = True, True

                # Transarency slider boolean
                is_cheating = config.developer or cheat_wardrobe_alpha
                is_blacklisted = self.type.startswith(self.blacklist_unequip)
                is_allowed = self.type.startswith(("makeup", "tattoo"))

                transparency = not is_blacklisted and (is_allowed or is_cheating)

                self.color[n] = color_picker(self.color[n], transparency, "Colour channel {}".format(n+1), pos_xy=(40, 85), color_default=self.color_default[n])
                self.char.override, self.override = False, False
            elif isinstance(n, list):
                self.color = [x[:] for x in n]
            self.rebuild_image()
            self.char.rebuild_image()
            self.build_icon()

        def reset_color(self, n=None):
            """Reset cloth color. Takes optional int layer number to reset only specific layer color."""
            if n:
                self.color[n] = [x for x in self.color_default]
            else:
                self.color = [x[:] for x in self.color_default]
            self.rebuild_image()
            self.char.rebuild_image()
            self.build_icon()

        def clone(self):
            """Creates a clone of this cloth object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            return DollCloth(self.name, self.categories, self.type, self.id, [x[:] for x in self.color], self.zorder, self.unlocked, self.level, self.blacklist, self, self.armfix, self.modpath)

        def set_pose(self, pose):
            for x in (self.categories[0], self.categories[1], self.type):
                if pose is None:
                    path = "{}/characters/{}/clothes/{}/{}/".format(self.modpath, self.name, x, self.id)
                    if renpy.loadable(path + "0.webp"):
                        self.imagepath = path
                        break
                else:
                    path = "{}/characters/{}/poses/{}/clothes/{}/{}/".format(self.modpath, self.name, pose, x, self.id)
                    if renpy.loadable(path + "0.webp"):
                        self.imagepath = path
                        break

            self.set_layers()
            self.rebuild_image()
            return

        def is_modded(self):
            """Returns True if item comes from a mod."""
            if self.modpath:
                return True
            return False

        def get_modname(self):
            """Return the name of the mod directory if exists."""
            return self.modpath.split("/")[1] if self.is_modded() else None
