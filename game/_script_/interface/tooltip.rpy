screen tooltip():
    layer "interface"
    tag tooltip
    zorder 5
    style_prefix "tooltip"

    if preferences.tooltip:
        $ tooltip = GetTooltip()
        $ x, y = renpy.get_mouse_pos()
        $ align = (1.0, 0.0) if x > config.screen_width/2 else (0.0, 0.0)

        if tooltip:
            window:
                background "#00000080"
                pos (x, y)
                anchor align
                align align
                text tooltip

style tooltip_window is empty:
    padding (5, 5)

style tooltip_text is default:
    color "#fff"
    size 12
    outlines [(1, "#00000080", 1, 0)]

init python:
    config.per_frame_screens.append("tooltip")
