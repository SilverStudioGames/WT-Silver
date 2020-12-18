init python:
    class DollFace(DollMethods):

        blacklist_blink = {"closed", "happyCl", "wink"}

        def __init__(self, obj, face):
            self.char = obj
            self.name = self.char.name
            self.face = face
            self.imagepath = "characters/{}/face/".format(self.name)
            self.blink = "spr_{} blink".format(self.name) if renpy.has_image("spr_{} blink".format(self.name)) else None

            self.rebuild_image()

        def build_image(self):
            sprites = []

            # Add facial expressions
            for k, v in self.face.iteritems():
                if v[0] and k != "pupils":
                    sprites.append(("{}{}/{}.webp".format(self.imagepath, k, v[0]), v[1]))

            eyes = self.face["eyes"][0]
            if settings.get('blinking') and self.blink and eyes not in self.blacklist_blink and not renpy.get_screen("studio"):
                sprites.append((self.blink, 10))

            path = "{}eyes/{}_mask.webp".format(self.imagepath, eyes)
            if renpy.loadable(path):
                pupils_path = "{}pupils/{}.webp".format(self.imagepath, self.face["pupils"][0])
                sprites.append((AlphaMask(pupils_path, path), self.face["pupils"][1]))

            sprites.sort(key=itemgetter(1))
            sprites = tuple(x[0] for x in sprites)
            return sprites

        def get_skin(self):
            for k, v in self.face.iteritems():
                skin_path = "{}{}/{}_skin.webp".format(self.imagepath, k, v[0])
                if renpy.loadable(skin_path):
                    yield skin_path

        def get_face(self):
            return dict((k, v[0]) for k, v in self.face.iteritems())

        def set_face(self, **kwargs):
            """Takes keyword argument(s) with the string name of expression file(s). Returns True if image is changed."""
            changed = False
            for arg, value in kwargs.iteritems():
                if value not in (self.face[str(arg)][0], False):
                    self.face[str(arg)][0] = value
                    changed = True

            if changed:
                self.rebuild_image()

            return changed

        def set_pose(self, pose):
            if pose is None:
                self.imagepath = "characters/{}/face/".format(self.name)
                blink_img = "spr_{} blink".format(self.name)
            else:
                self.imagepath = "characters/{}/poses/{}/face/".format(self.name, pose)
                blink_img = "spr_{} blink {}".format(self.name, pose)

            self.blink = blink_img if renpy.has_image(blink_img) else None
            self.rebuild_image()
            return

        def set_zorder(self, **kwargs):
            """Takes keyword argument(s) with the string name of face type(s) and int value(s). Returns True if image is changed."""
            changed = False
            for arg, value in kwargs.iteritems():
                if value != self.face[str(arg)][1]:
                    self.face[str(arg)][1] = value
                    changed = True

            if changed:
                self.rebuild_image()

            return changed
