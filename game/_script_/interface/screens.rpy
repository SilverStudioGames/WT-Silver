screen dropdown_menu(pos=(0, 0), name="", spacing=0, items_offset=(0, 0), background="#00000080", style="empty", iconset=["▾", "▴"]):
    tag dropdown
    modal True
    default visible = False
    default iconset = iconset
    default icon = iconset[0]

    if visible:
        use invisible_button(action=[SetLocalVariable("visible", False), SetLocalVariable("icon", iconset[0])])

    window:
        style "empty"
        pos pos

        textbutton "[name] {unicode}{size=+1}[icon]{/size}{/unicode}":
            style style
            ysize 24
            text_yalign 0.5
            text_size 12
            text_hover_color "#FFF"
            action [ToggleLocalVariable("visible", True, False), ToggleLocalVariable("icon", iconset[0], iconset[1])]
        if visible:
            frame:
                pos (0, 24)
                style "empty"
                offset items_offset
                background background
                padding (5, 5, 5, 5)
                vbox:
                    spacing spacing
                    transclude

#Close Button
screen close_button(xoffset=0, yoffset=0, action=Return("Close")):

    # Restore menu access if we're leaving nested context
    if renpy.context_nesting_level() == 1:
        $ action = [Function(enable_game_menu), action]

    imagebutton:
        xalign 1.0
        xanchor 1.0
        offset (xoffset, yoffset)
        idle gui.format("interface/topbar/buttons/{}/ui_close.webp")
        hover image_hover(gui.format("interface/topbar/buttons/{}/ui_close.webp"))
        action action
        keysym "game_menu"

screen close_button_background(action=Return("Close"), keysym=None):

    # Restore menu access if we're leaving nested context
    if renpy.context_nesting_level() == 1:
        $ action = [Function(enable_game_menu), action]

    # Note: Actions cannot be passed as transclude, separate parameter is required.
    button style "empty":
        action action
        keysym keysym
        transclude

# Animation effect controller
screen gfx_effect(start_x=None, start_y=None, target_x=None, target_y=None, img, xanchor=0.5, yanchor=0.5, zoom=0.5, duration=1.0, timer=0.5):
    tag gfx
    zorder 30

    if target_x:
        add img xanchor xanchor yanchor yanchor zoom zoom at move_to(start_x, start_y, target_x, target_y, duration)
    else:
        add img xanchor xanchor yanchor yanchor zoom zoom xpos start_x ypos start_y
    timer timer action Hide("gfx_effect")

screen ctc():
    zorder 30
    add "ctc"
