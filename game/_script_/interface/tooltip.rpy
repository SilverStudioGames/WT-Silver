screen tooltip():
    layer "interface"
    tag tooltip
    zorder 5
    style_prefix "tooltip"

    default last_tooltip = None
    default show_tooltip = False

    if preferences.tooltip:
        $ tooltip = GetTooltip()

        if tooltip == last_tooltip:
            timer 0.5 action SetScreenVariable("show_tooltip", True)
        else:
            $ last_tooltip = tooltip
            $ show_tooltip = False

        if tooltip and show_tooltip:
            $ x, y = renpy.get_mouse_pos()
            $ flip = x > config.screen_width / 2
            $ align = (1.0, 0.0) if flip else (0.0, 0.0)

            window:
                background "#00000080"
                offset (-5 if flip else 10, 5)
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
