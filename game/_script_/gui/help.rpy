
init offset = -1

screen help(page='tutorials'):
    tag menu

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 8
            null # Tab margin

            if page == 'tutorials':
                use tutorials_help
            elif page == "controls":
                use controls_help
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
            textbutton _("Controls") action [SelectedIf(page == 'controls'), Show("help", config.intra_transition, "controls")]
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

screen controls_help():

    hbox:
        label _("Interaction")
        text _("Space, Enter or Left Mouse Button")

    hbox:
        label _("Navigate Interface")
        text _("Arrow keys or mouse")

    hbox:
        label _("Cancel/Menu")
        text _("Escape or Right Mouse Button")

    hbox:
        label _("Skipping")
        text _("Ctrl")

    hbox:
        label _("Toggle Skipping")
        text _("Tab")

    hbox:
        label _("Roll Back")
        text _("Page Up or Mouse Wheel Up")

    hbox:
        label _("Roll Forward")
        text _("Page Down or Mouse Wheel Down")

    hbox:
        label "Hide Interface"
        text _("H or Middle Mouse Button")

    hbox:
        label "Screenshot"
        text _("Print Screen")

    hbox:
        label "Sleep"
        text _("s")

    hbox:
        label "Map"
        text _("m")

    hbox:
        label "Stats"
        text _("c")

    hbox:
        label "Inventory"
        text _("i")

    hbox:
        label "Fap-Fap-Fap"
        text _("f")

    hbox:
        label "Summon"
        text _("d")

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
