init python:
    # TODO: Buggy.
    def preserve_aspect_ratio(target_w, target_h):
        if ( not renpy.mobile and pygame.display.get_init() and renpy.display.draw
            and settings.get('preserve_aspect_ratio') and not preferences.fullscreen ):
            aspect_ratio = target_w / target_h

            if aspect_ratio != 1.8:
                if target_w > target_h:
                    target_h = int(target_w / 1.8)
                else:
                    target_w = int(target_h * 1.8)

                renpy.set_physical_size((target_w, target_h))
        return (target_w, target_h)

    #config.adjust_view_size = preserve_aspect_ratio
