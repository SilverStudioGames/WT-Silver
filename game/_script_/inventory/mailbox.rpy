
init python:
    class Mailbox(object):
        def __init__(self):
            self.parcels = []
            self.letters = []

        def get_parcels(self, raw=False):
            return self.parcels if raw else [x for x in self.parcels if x.wait < 1]
        def get_letters(self, raw=False):
            return self.letters if raw else [x for x in self.letters if x.wait < 1]

        def tick(self):
            """Causes time to pass."""
            for i in self.parcels:
                i.wait -= 1

            for i in self.letters:
                i.wait -= 1

        def type_in_parcels(self, type):
            """Returns true if item type found in any of the parcel contents."""
            if type == "outfit":
                return any( isinstance(y[0], DollOutfit) for x in self.parcels for y in x.contents )
            return any( (y[0].type == type) for x in self.parcels for y in x.contents )

init offset = -1
default mailbox = Mailbox()
