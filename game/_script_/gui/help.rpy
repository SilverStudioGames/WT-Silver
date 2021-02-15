#
# Help screen
#
# A screen that gives information about key and mouse bindings. It uses other
# screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
# help.

init offset = -1

screen help(page='tutorials'):
    tag menu

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13
            null # Tab margin

            if page == 'tutorials':
                use tutorials_help
            elif page == "keyboard":
                use keyboard_help
            elif page == "mouse":
                use mouse_help
            elif page == "gamepad":
                use gamepad_help
            elif page == "about":
                use about_help

    hbox:
        style_prefix gui.theme("tab")
        pos (25 + 15, 100)
        yanchor 0.5

        textbutton _("Tutorials") action [SelectedIf(page == 'tutorials'), Show("help", config.intra_transition, "tutorials")]
        if not renpy.mobile:
            textbutton _("Keyboard") action [SelectedIf(page == 'keyboard'), Show("help", config.intra_transition, "keyboard")]
            textbutton _("Mouse") action [SelectedIf(page == 'mouse'), Show("help", config.intra_transition, "mouse")]
        if GamepadExists():
            textbutton _("Gamepad") action [SelectedIf(page == 'gamepad'), Show("help", config.intra_transition, "gamepad")]
        textbutton _("About") action [SelectedIf(page == 'about'), Show("help", config.intra_transition, "about")]

screen tutorials_help():
    for entry, tutorial in tutorial_dict.iteritems():
        $ title = tutorial[0]

        textbutton "[title]":
            action Function(renpy.call_in_new_context, 'tutorials_help', entry)
            # action ShowTransient('tutorial', None, entry)
            # sensitive tutorial_is_done(entry)

label tutorials_help(entry):
    show screen help('tutorials')
    $ renpy.play("sounds/pop01.mp3")
    $ renpy.music.set_volume(0.5, 3.0)
    call screen tutorial(entry)
    $ renpy.music.set_volume(1.0, 3.0)
    return

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

screen about_help():
    vbox:
        spacing gui.pref_spacing

        if gui.about:
            text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") size 12

style help_button is gui_button:
    background None
    xmargin 7

style help_button_text is gui_button_text

style help_label is gui_label:
    xsize 209
    right_padding 17

style help_label_text is gui_label_text:
    xalign 1.0
    text_align 1.0
    outlines [(2, "#000", 0, 0)]

style help_text is gui_text
