init python:
    class DollLipstick(DollCloth):

        def set_imagepath(self):
            self.imagepath = "{}/characters/{}/clothes/makeup/lipstick/".format(self.modpath, self.name)

        def set_layers(self):
            for x in self.layers_special:
                self.__dict__[x] =  None

            for x in self.layers_additional:
                self.__dict__[x] = []
                for i in xrange(self.layers):
                    path = "{}{}_{}.webp".format(self.imagepath, i, x)
                    if renpy.loadable(path):
                        self.__dict__[x].append(path)
                self.__dict__[x+"_outline"] = None

            return

        def build_image(self):
            mouth = self.char.face.face["mouth"][0]
            sprites = ((self.apply_color("{}{}.webp".format(self.imagepath, mouth), 0)), )
            return sprites

        def build_icon(self):
            mouth = self.char.face.face["mouth"][0]
            bounds = "{}{}.webp".format(self.imagepath, mouth)
            self.ico = CroppedImage(self.build_image(), bounds)

        def set_pose(self, pose):
            if pose is None:
                path = "{}/characters/{}/clothes/makeup/lipstick/".format(self.modpath, self.name)
                self.imagepath = path
            else:
                path = "{}/characters/{}/poses/{}/clothes/makeup/lipstick/".format(self.modpath, self.name, pose)
                if renpy.loadable(path + "base.webp"):
                    self.imagepath = path

            self.rebuild_image()
            return

        def clone(self):
            """Creates a clone of this lipstick object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            return DollLipstick(self.name, self.categories, self.type, self.id, [x[:] for x in self.color], self.zorder, self.unlocked, self.level, self.blacklist, self, self.armfix, self.modpath)
