
init -1 python:

    class Room(object):
        def __init__(self, id):
            self.id = id
            self.objects = set()

        def add(self, obj):
            self.objects.add(obj)

        def remove(self, obj):
            self.objects.remove(obj)

    class RoomObject(object):

        def __init__(self, room, id, pos, idle, hover=None, foreground=None, background=None, anchor=(0.5, 0.5), focus_mask=True, action=NullAction(), hovered=None, unhovered=None, tooltip=None, decoration=None):
            self.room = room
            self.id = id
            self.pos = pos
            self.idle = idle
            self.hover = hover or self.idle
            self.foreground = foreground
            self.background = background
            self.anchor = anchor
            self.focus_mask = focus_mask
            self.action = action
            self.hovered = hovered
            self.unhovered = unhovered
            self.tooltip = tooltip
            self.decoration = decoration
            self.hidden = False

            # Add to the main room if room was specified
            if self.room:
                self.room.add(self)

            # Backwards compatibility, to be resolved if possible.
            self.xpos, self.ypos = self.pos

        def get_idle(self):
            if self.hidden:
                return Null()

            if self.decoration:
                return Fixed(self.idle, self.decoration.image)
            return self.idle

        def get_hover(self):
            if self.hidden:
                return Null()

            if self.decoration:
                return Transform(Fixed(self.hover, self.decoration.image), shader="outline_shader")
            return Transform(self.hover, shader="outline_shader")

