
init python:
    class Mailbox(object):
        def __init__(self):
            self.parcels = []
            self.letters = []

        def get_parcels(self):
            return [x for x in self.parcels if x.wait < 1]

        def get_letters(self):
            return [x for x in self.letters if x.wait < 1]

        def tick(self):
            """Causes time to pass."""
            for i in self.parcels:
                i.wait -= 1

            for i in self.letters:
                i.wait -= 1

init offset = -1
default mailbox = Mailbox()
