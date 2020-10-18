
init -1 python:

    ### Global Functions ###

    def get_character_emote(char, emote):
        return "characters/{}/emotes/{}.webp".format(char, emote) if emote else None

    def get_character_pos(char):
        global sprite_pos

        flip = getattr(renpy.store, char+"_flip", None)
        use_head = getattr(renpy.store, "use_"+char+"_head", None)

        # Resolve X position for head state
        if use_head:
            xpos = sprite_pos["x"]["far_right"] if flip == 1 else sprite_pos["x"]["far_left"]
        else:
            xpos = getattr(renpy.store, char+"_xpos", None)
        ypos = getattr(renpy.store, char+"_ypos", None)

        return (xpos, ypos)

    ### Classes ###

    class DollMethods(object):
        """Container class for commonly used methods and attributes"""
        sprite = None
        cached = False
        override = False

        layers_extra = {"extra", "outline", "overlay"}
        layers_special = {"skin", "mask", "wind_mask"}
        layers_additional = {"back", "front"}

        blacklist_toggles = {"hair", "pubes", "piercing", "makeup", "tattoo", "accessory"}
        blacklist_unequip = {"hair"}

        def rebuild_image(self):
            # Defers rebuild until next time get_image is called
            self.cached = False

        def get_image(self):
            if not renpy.is_skipping() or self.sprite is None:
                if self.override:
                    sprites = self.build_image()
                    self.sprite = Fixed(*sprites, fit_first=True)
                elif not self.cached:
                    sprites = self.build_image()
                    self.sprite = Fixed(*sprites, fit_first=True)
                    self.cached = True
            return self.sprite

    # Wrapping the child displayable somehow makes it perform better with drag and drop
    class DollDisplayable(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(DollDisplayable, self).__init__(**kwargs)
            self.child = renpy.displayable(child)

        def render(self, w, h, st, at):
            cr = renpy.display.render.render(self.child, w, h, st, at)
            cw, ch = cr.get_size()
            rv = renpy.display.render.Render(cw, ch)
            rv.blit(cr, (0, 0), focus=False)

            return rv

        def event(self, ev, x, y, st):
            return None

        def visit(self):
            return [ self.child ]
