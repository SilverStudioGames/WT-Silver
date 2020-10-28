
init python:

    class Item(object):
        _instances = set() # TODO: Somehow the object references change after renpy restart, but doesn't crash?

        def __init__(self, id, type, name, price=0, desc="", unlocked=True, func=None, label=None, limit=100, image="default"):
            self.id = id
            self.type = type
            self.name = name
            self.price = price
            self.desc = desc
            self.unlocked = unlocked
            self.func = func
            self.label = label
            self.limit = limit
            self.image = "interface/icons/{}.webp".format(self.id) if image == "default" else image

            self.usable = bool(self.func or self.label)
            self.used = False
            self._owned = 0
            self._instances.add(self)

        def use(self):
            if not self.usable:
                raise Exception("Item '{}' is not usable as it does not have any function or a label.".format(self.name))

            self.used = True

            if self.func:
                self.func()

            if self.label:
                renpy.jump_out_of_context(self.label)

        def get_image(self):
            if isinstance(self.image, basestring):
                return self.image
            else:
                return self.image()

        @classmethod
        def get_instances(cls):
            return cls._instances

        @classmethod
        def get_instances_of_type(cls, type):
            return filter(lambda x: x.type == type, cls.get_instances())

        @property
        def owned(self):
            return self._owned

        @owned.setter
        def owned(self, value):
            self._owned = max(min(value, self.limit), 0)
