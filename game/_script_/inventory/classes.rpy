init python:

    class Inventory(object):
        def __init__(self):
            self.items = set()

        def add(self, item):
            self.items.add(item)

        def remove(self, item):
            self.items.remove(item)

        def get_instances(self):
            return self.items

        def get_instances_of_type(self, type):
            return filter(lambda x: x.type == type, self.get_instances())

    class Item(object):
        _instances = [] # TODO: Somehow the object references change after renpy restart, but doesn't crash?

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

            inventory.add(self)

        def use(self):
            if not self.usable:
                raise Exception("Item '{}' is not usable as it does not have any function or a label.".format(self.name))

            if self.owned == 0:
                raise Exception("Item '{}' owned count is equal to zero.".format(self.name))

            self.used = True

            if self.func:
                self.func()

            if self.label:
                if renpy.context_nesting_level() > 0:
                    renpy.jump_out_of_context(self.label)
                else:
                    renpy.jump(self.label)

        def get_image(self):
            if isinstance(self.image, basestring):
                return self.image
            else:
                return self.image()

        @property
        def owned(self):
            return self._owned

        @owned.setter
        def owned(self, value):
            if not self.unlocked:
                self.unlocked = True

            self._owned = max(min(value, self.limit), 0)

init offset = -5

default inventory = Inventory()
