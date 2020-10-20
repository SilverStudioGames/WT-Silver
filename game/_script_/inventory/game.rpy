init python:
    def show_gold(st, at, old, new):
        if st > 1.0:
            return Text("G {}".format(new)), None
        else:
            if new > old:
                value = int( (new-old)*(1.0-st) )
                d = Text("G {}\n+{}".format(old + int((new-old)*st), value))
            else:
                value = int( (old-new)*(1.0-st) )
                d = Text("G {}\n-{}".format(old - int((old-new)*st), value))
            return d, 0.01

    class Game(object):
        def __init__(self, gold=0, day=1):
            # Protected values
            self._gold = gold
            self._day = day
            self._gryf = 0
            self._slyt = 0
            self._rave = 0
            self._huff = 0

            # Normal values
            self.daytime = True
            self.difficulty = 2
            self.cheats = False

        @property
        def gold(self):
            return self._gold

        @gold.setter
        def gold(self, value):
            old = self._gold
            self._gold = max(0, min(value, 99999))

            if not renpy.in_rollback():
                renpy.hide_screen("gold")
                renpy.show_screen("gold", old, self._gold)

        @property
        def day(self):
            return self._day

        @day.setter
        def day(self, value):
            self._day = max(1, min(value, 99999))

screen gold(old, new):
    tag gold
    zorder 50

    frame:
        xpadding 10
        ysize 44
        xminimum 80
        background Frame(gui.format("interface/frames/{}/iconmed.webp"), 6, 6)
        pos (50, 50)

        add DynamicDisplayable(show_gold, old, new) yoffset 3

    timer 3.0 action Hide("gold")

default game = Game()

# Points change displayable
# Day change displayable
# Add one of X generator
