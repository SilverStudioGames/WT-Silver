default deliveries = DeliveryQueue()

label get_package:
    show screen blktone

    if clothing_mail_item != None:
        if clothing_mail_timer <= 0:
            call unlock_clothing(text="You have received a new outfit.", item=clothing_mail_item)
            $ clothing_mail_item = None
            $ clothing_mail_timer = 0

    python:
        gift_list = []

        # Append gift items
        for item in deliveries.get_mail():
            if item.type == 'Gift':
                gift = item.item
                gift.number += item.quantity
                gift_list.append([gift.name, gift.get_image(), item.quantity])

        if gift_list:
            renpy.block_rollback()
            renpy.call("give_reward", *parcel.get_caption())

    hide screen package
    hide screen blktone
    with d3

    $ package_is_here = False
    $ renpy.block_rollback()

    call tutorial("inventory")

    jump main_room_menu

init python:

    class DeliveryItem(object):
        def __init__(self, item, transit_time, quantity,type):
            self.item = item
            self.transit_time = transit_time
            self.quantity = quantity
            self.type = type

    class DeliveryQueue(object):
        max_wait = 15

        def __init__(self):
            self.queue = []

        def send(self, item, transit_time, quantity, type):
            if transit_time > self.max_wait:
                transit_time = self.max_wait
            self.queue.append(DeliveryItem(item, transit_time, quantity, type))

        def got_mail(self):
            for i in self.queue:
                i.transit_time -= 1
            for i in self.queue:
                if i.transit_time <= 0:
                    return True
            return False

        def get_mail(self):
            delivery = []
            for i in list(self.queue):
                if i.transit_time <= 0:
                    delivery.append(i)
                    self.queue.remove(i)
            return delivery

    ### UNFINISHED, TBD IN NEXT COMMIT ###
    class Parcel(object):
        queue = []

        def __init__(self, contents=[], wait=1):
            self.mailed = False
            self.delivered = False
            self.contents = contents
            self.wait = wait

        def send(self):
            self.mailed = True

            if not self in self.queue:
                self.queue.append(self)

        def open(self):
            self.delivered = True

            if self in self.queue:
                self.queue.remove(self)

        def get_caption(self):
            if len(self.contents) == 1:
                item = self.contents[0]
                icon = item.get_image()

                if item.quantity == 1:
                    text = "You have received {}.".format(item.name)
                else:
                    text = "You have received {} pieces of {}.".format(num_to_word(item.quantity), item.name)
            else:
                items = ", ".join( [" ".join( str(x.quantity), x.name ) for x in self.contents] )
                icon = "interface/icons/box_brown_"+str(random.randint(1, 4))+".webp"
                text = "You have received your ordered items:\n{size=-4}{}{/size}".format(items)

            return (text, icon)
