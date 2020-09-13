init python:
    class DollBody(DollMethods):
        zorder_skin = 5

        def __init__(self, obj, body):
            self.char = obj
            self.name = self.char.name
            self.body = body
            self.hue = 0
            self.imagepath = "characters/{}/body/".format(self.name)

            self.rebuild_image()

        def build_image(self):
            sprites = []

            # Add body parts and skin layers from clothes, face, cum
            sprites.extend(("{}{}/{}.webp".format(self.imagepath, k, v[0]), v[1]) for k, v in self.body.iteritems() if v[0]) # Body parts
            sprites.extend((o[0].skin, self.zorder_skin) for o in self.char.clothes.itervalues() if o[0] and o[0].skin and o[2]) # Clothes skin
            sprites.extend((x, self.zorder_skin) for x in self.char.face.get_skin()) # Face skin
            sprites.extend((x, self.zorder_skin) for x in self.char.cum.get_skin()) # Cum skin

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable( ((0,0), Transform(x[0], matrixcolor=HueMatrix(self.hue)) ) for x in sprites))
            return sprites

        def build_mannequin(self, group=None):
            sprites = []

            # Add body parts and skin layers from clothes
            sprites.extend(("{}{}/{}.webp".format(self.imagepath, k, v[0]), v[1]) for k, v in self.body.iteritems() if v[0])
            if group:
                sprites.extend((o.skin, self.zorder_skin) for o in group if o and o.skin)

            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), im.Grayscale(x[0])) for x in sprites))
            return sprites

        def get_mannequin(self, group=None):
            mannequin = self.build_mannequin(group)
            return Composite(self.size, *mannequin)

        def get_part(self, arg):
            return self.body[arg][0]

        def set_body(self, **kwargs):
            """Takes keyword argument(s) with the string name of body part file(s). Returns True if image is changed."""
            changed = False

            for arg, value in kwargs.iteritems():
                if value != self.body[str(arg)][0]:
                    self.body[str(arg)][0] = value
                    changed = True

            if changed:
                self.rebuild_image()

            return changed

        def set_pose(self, pose):
            if pose is None:
                self.imagepath = "characters/{}/body/".format(self.name)
            else:
                self.imagepath = "characters/{}/poses/{}/body/".format(self.name, pose)
            self.rebuild_image()
            return

        def set_zorder(self, **kwargs):
            """Takes keyword argument(s) with the string name of body type(s) and int value(s). Returns True if image is changed."""
            changed = False

            for arg, value in kwargs.iteritems():
                if value != self.body[str(arg)][1]:
                    self.body[str(arg)][1] = value
                    changed = True

            if changed:
                self.rebuild_image()

            return changed
