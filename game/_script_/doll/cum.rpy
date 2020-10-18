init python:
    class DollCum(DollMethods):
        zorder_cum = 100

        def __init__(self, obj):
            self.char = obj
            self.name = self.char.name
            self.imagepath = "characters/{}/cum/".format(self.name)

            self.cum = dict((k, None) for k in {"hair", "face", "breasts", "body", "crotch", "pussy", "legs"})

            self.rebuild_image()

        def build_image(self):
            sprites = tuple("{}{}/{}.webp".format(self.imagepath, k, v) for k, v in self.cum.iteritems() if v != None)
            return sprites

        def get_skin(self):
            return ["{}{}/{}_skin.webp".format(self.imagepath, k, v) for k, v in self.cum.iteritems() if renpy.loadable("{}{}/{}_skin.webp".format(self.imagepath, k, v))]

        def set_cum(self, *args, **kwargs):
            """Takes keyword argument(s) containing string name(s) of cum layers to apply or None. Returns True if image is changed."""
            changed = False

            if args:
                for k, v in self.cum.iteritems():
                    if v != args[0]:
                        self.cum[k] = args[0]
                        changed = True

            for arg, value in kwargs.iteritems():
                if str(arg) != value:
                    self.cum[str(arg)] = value
                    changed = True

            if changed:
                self.rebuild_image()

            return changed

        def set_pose(self, pose):
            if pose is None:
                self.imagepath = "characters/{}/cum/".format(self.name)
            else:
                self.imagepath = "characters/{}/poses/{}/cum/".format(self.name, pose)
            self.rebuild_image()
            return
