#
# Additional screens
#

init offset = -1

# Confirm screen
#
# The confirm screen is called when Ren'Py wants to ask the player a yes or no
# question.
#
# https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action=Return(True), no_action=Return(False)):
    modal True

    zorder 200

    style_prefix gui.theme()

    add "confirm_fade"

    frame:
        padding (34, 34, 34, 34)
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 25

            text _(message):
                xalign 0.5
                text_align 0.5

            hbox:
                xalign 0.5
                spacing 84

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

image confirm_fade:
    Solid("#000")
    alpha 0.0

    on appear:
        alpha 0.5
    on show:
        linear 0.3 alpha 0.5
    on hide:
        linear 0.3 alpha 0.0

style confirm_frame is gui_frame:
    padding (34, 34, 34, 34)
    xalign 0.5
    yalign 0.5

style dark_confirm_frame is dark_gui_frame:
    take confirm_frame

style light_confirm_frame is light_gui_frame:
    take confirm_frame

# Skip indicator screen
#
# The skip_indicator screen is displayed to indicate that skipping is in
# progress.
#
# https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():
    zorder 100

    text "{unicode}{size=66}▶▶{/size}{/unicode}\nSkipping":
        at blink
        style "skip_text"

style skip_text is default:
    size 22
    text_align 0.5
    pos (50, 50)
    color "#fff"
    outlines [(1, "#00000080", 1, 0)]

# Notify screen
#
# The notify screen is used to show the player a message. (For example, when
# the game is quicksaved or a screenshot has been taken.)
#
# https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):
    layer "interface"
    sensitive False

    frame at notify_appear:
        align (0.0, 1.0)
        text message: # or "[message!tq]"
            color "#fff"
            outlines [(1, "#00000080", 1, 0)]

    timer 3.25 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_text is gui_text

style notify_frame is empty:
    background Frame("gui/notify.png")
    padding (4, 4, 4, 4)

style notify_text:
    size 14
