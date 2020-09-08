
init python:
    class Parcel(object):
        """
        contents - Contents of the parcel, has to be a list of tuples
                   containing an item object and integer quantity [ (lollipop_ITEM, 5) ].
        wait - Wait time required for the item to be delivered.
        label - Call label called after the parcel was opened.
        func - A setup function called before the parcel contents is being shown to the player.

        Queue is universal for all instanced objects.
        """

        def __init__(self, contents, wait=1, label=None, func=None):
            self.mailed = False
            self.delivered = False
            self.contents = contents
            self.wait = wait
            self.label = label
            self.func = func
            self.queue = mailbox.parcels

        def send(self):
            self.mailed = True

            if not self in self.queue:
                self.queue.append(self)

        def open(self, silent=False):
            self.mailed = True
            self.delivered = True

            if self in self.queue:
                self.queue.remove(self)

            if self.func:
                self.func()

            for i in self.contents:
                item, quantity = i
                item.number += quantity

            if not silent:
                renpy.call("parcel", self, self.label)

        def get_caption(self):
            if len(self.contents) == 1:
                item, quantity = self.contents[0]
                icon = item.get_image()

                if quantity == 1:
                    text = "You have received {}.".format(item.name)
                else:
                    text = "You have received {} pieces of {}.".format(num_to_word(quantity), item.name)
            else:
                items = ", ".join( [" ".join( str(x[1]), x[0].name ) for x in self.contents] )
                icon = "interface/icons/box_brown_"+str(random.randint(1, 4))+".webp"
                text = "You have received your ordered items:\n{size=-4}{}{/size}".format(items)

            return (text, icon)

label parcel(parcel, label):
    show screen bld1
    show screen blktone5

    $ renpy.checkpoint()
    $ renpy.call("give_reward", *parcel.get_caption())

    hide screen blktone5
    hide screen bld1
    with d3

    if label:
        $ renpy.call(label)

    return

label parcel_open_all:
    while mailbox.get_parcels():
        $ mailbox.get_parcels()[0].open()

    hide screen package
    call tutorial("inventory")

    jump main_room_menu
