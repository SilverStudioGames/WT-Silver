screen tooltip():
    layer "interface"
    tag tooltip
    zorder 5
    style_prefix "tooltip"

    if settings.get("tooltip"):
        default last_tooltip = None

        $ tooltip = GetTooltip()

        if tooltip != last_tooltip:
            timer 0.5 action SetScreenVariable("last_tooltip", tooltip)
        elif tooltip:
            $ last_tooltip = tooltip
            $ x, y = renpy.get_mouse_pos()
            $ flip = x > config.screen_width / 2
            $ align = (1.0, 0.0) if flip else (0.0, 0.0)
            $ offset = (0, 5) if flip else (10, 5)

            window:
                offset offset
                pos (x, y)
                anchor align
                align align
                text tooltip

style tooltip_window is empty:
    background "#00000080"
    padding (5, 5)

style tooltip_text is default:
    color "#fff"
    size 12
    outlines [(1, "#00000080", 1, 0)]

init python:
    config.per_frame_screens.append("tooltip")
