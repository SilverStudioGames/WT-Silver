#
# Preferences screen
#
# The preferences screen allows the player to configure the game to better suit
# themselves.
#
# https://www.renpy.org/doc/html/screen_special.html#preferences

init offset = -1

screen preferences(page="options"):
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):
        style_prefix gui.theme("pref")

        vbox:
            spacing gui.pref_spacing
            null # Tab margin

            if page == 'options':
                use preferences_options
            elif page == 'graphics':
                use preferences_graphics

    hbox:
        style_prefix gui.theme("tab")
        pos (25 + 15, 100)
        yanchor 0.5

        textbutton "Options" action [
            SelectedIf(page == 'options'),
            Show('preferences', config.intra_transition, 'options')
        ]
        textbutton "Graphics"  action [
            SelectedIf(page == 'graphics'),
            Show('preferences', config.intra_transition, 'graphics')
        ]

screen preferences_options():
    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("check")

            label _("Interface")
            textbutton "Tutorials"
            textbutton _("Tooltips") action ToggleVariable("preferences.tooltip", True, False)
            textbutton _("Custom Cursor") action [
                ToggleVariable("preferences.customcursor", True, False),
                # Broken in 7.4 nightly: ToggleVariable("config.mouse", { 'default' : [ ('interface/cursor.webp', 0, 0)] }, None)
            ]

        default trans = config.intra_transition

        vbox:
            style_prefix gui.theme("radio")

            label "Theme"
            textbutton "Auto" action [
                settings.Set('theme', 'auto'),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]
            textbutton "Day" action [
                settings.Set('theme', 'light'),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]
            textbutton "Night" action [
                settings.Set('theme', 'dark'),
                Function(renpy.transition, trans),
                Function(renpy.restart_interaction)
            ]

        vbox:
            style_prefix gui.theme("pref")

            $ text_color_day = settings.get('text_color_day')
            $ text_color_night = settings.get('text_color_night')

            label _("Text Colour")
            default color_square = "{font=[gui.glyph_font]}❖{/font}"

            hbox:
                textbutton "Day" size_group "text_color" action [
                        Function(renpy.invoke_in_new_context, pick_color_setting, "text_color_day", "Day text colour"),
                        Function(renpy.transition, trans),
                        Function(gui.rebuild_styles)
                    ]
                textbutton "{color=[text_color_day]}[color_square!i]{/color}" yalign 0.5 style "empty" background "#d1a261"
                textbutton "Reset" text_size 14 yalign 0.5 padding (0, 0) action [
                        settings.Reset("text_color_day"),
                        Function(renpy.transition, trans),
                        Function(gui.rebuild_styles)
                    ]

            hbox:
                textbutton "Night" size_group "text_color" action [
                        Function(renpy.invoke_in_new_context, pick_color_setting, "text_color_night", "Night text colour"),
                        Function(renpy.transition, trans),
                        Function(gui.rebuild_styles)
                    ]
                textbutton "{color=[text_color_night]}[color_square!i]{/color}" yalign 0.5 style "empty" background "#5b4f4f"
                textbutton "Reset" text_size 14 yalign 0.5 padding (0, 0) action [
                        settings.Reset("text_color_night"),
                        Function(renpy.transition, trans),
                        Function(gui.rebuild_styles)
                    ]

            hbox:
                textbutton "Outline" size_group "text_color" action Function(print, "text_shadow")

        vbox:
            style_prefix gui.theme("check")
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("slider")
            spacing gui.pref_spacing / 2

            label _("Text Speed")
            bar value Preference("text speed")

            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")

            label _("Text Scaling")
            hbox:
                xalign 0.25
                textbutton "XS" action Preference("font size", 0.7)
                textbutton "S" action Preference("font size", 0.9)
                textbutton "Normal" action Preference("font size", 1.0)
                textbutton "L" action Preference("font size", 1.2)
                textbutton "XL" action Preference("font size", 1.4)

        vbox:
            style_prefix gui.theme("slider")
            spacing gui.pref_spacing / 2

            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume")

            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

                label _("Weather Volume")
                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

            if config.has_voice:
                label _("Voice Volume")
                hbox:
                    bar value Preference("voice volume")
                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"
    hbox:
        box_wrap True

        vbox:
            style_prefix gui.theme("check")

            label _("Advanced")
            textbutton _("Autosave"):
                action [
                    ToggleVariable("persistent.autosave", True, False),
                    Notify("Autosave preference will take effect after restarting the game")
                ]
            textbutton _("Confirm Delete"):
                action ToggleVariable("persistent.save_confirm_delete", True, False)
            textbutton "Full reset":
                style gui.theme("pref_button")
                action Confirm(gui.CONFIRM_FULL_RESET, Function(delete_persistent))

define gui.CONFIRM_FULL_RESET = """{color=#f00}Warning!{/color}
This will clear everything except for saves!

{size=-4}Reset persistent data, such as
achievements, seen text, and preferences.{/size}

Are you sure you want to perform a full reset of the game?"""

screen preferences_graphics():
    hbox:
        box_wrap True

        if renpy.variant("pc") or renpy.variant("web"):
            vbox:
                style_prefix gui.theme("radio")
                label _("Display")
                textbutton _("Default"):
                    action Preference("display", "window")
                    sensitive (renpy.get_physical_size() != (config.screen_width, config.screen_height))
                textbutton _("Window") action Preference("display", "any window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

        vbox:
            style_prefix gui.theme("radio")

            default fps_msg = "Framerate preference may take effect after restarting the game"

            label "Framerate"
            textbutton "Screen" action [Preference("gl framerate", None), Notify(fps_msg)]
            textbutton "60 fps" action [Preference("gl framerate", 60), Notify(fps_msg)]
            textbutton "30 fps" action [Preference("gl framerate", 30), Notify(fps_msg)]


        vbox:
            style_prefix gui.theme("pref")

            label "Ren'Py"
            textbutton "Accessibility" action Show("_accessibility")
            textbutton "Rendering" action [
                Function(renpy.call_in_new_context, "_choose_renderer"),
                Notify("Rendering preferences may take effect after restarting the game")
            ]

init python:
    def delete_persistent():
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.quit(relaunch=True)

    def pick_color_setting(setting_name, title):
        renpy.show_screen("preferences")
        color = settings.get(setting_name)
        r, g, b, _ = color_picker(get_rgb_list(color), False, title)
        color = get_hex_string(r/255.0, g/255.0, b/255.0)
        settings.set(setting_name, color)

style mute_all_button is check_button
style mute_all_button_text is check_button_text

# Preference

style pref_label is gui_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text is gui_label_text:
    yalign 1.0

style dark_pref_label_text is dark_label_text
style light_pref_label_text is light_label_text

style pref_button is gui_button:
    padding (18, 4, 4, 4)

style pref_button_text is gui_button_text

style pref_vbox is vbox:
    xminimum (245 - 30 - 60) / 2

style pref_hbox:
    spacing 30
    box_wrap_spacing 2 * gui.pref_spacing

# Radio button

style radio_label is pref_label
style radio_label_text is pref_label_text
style dark_radio_label_text is dark_pref_label_text
style light_radio_label_text is light_pref_label_text

style radio_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style radio_button is gui_button:
    background None
    padding (18, 4, 4, 4)

style dark_radio_button is dark_gui_button:
    take radio_button
    foreground "gui/button/dark_radio_[prefix_]foreground.png"

style light_radio_button is light_gui_button:
    take radio_button
    foreground "gui/button/light_radio_[prefix_]foreground.png"

style radio_button_text is gui_button_text

# Check button

style check_label is pref_label
style check_label_text is pref_label_text
style dark_check_label_text is dark_pref_label_text
style light_check_label_text is light_pref_label_text

style check_vbox is pref_vbox:
    spacing gui.pref_button_spacing

style check_button is gui_button:
    background None
    padding (18, 4, 4, 4)

style dark_check_button is dark_gui_button:
    take check_button
    foreground "gui/button/dark_check_[prefix_]foreground.png"

style light_check_button is light_gui_button:
    take check_button
    foreground "gui/button/light_check_[prefix_]foreground.png"

style check_button_text is gui_button_text

# Slider

style slider_label is pref_label
style slider_label_text is pref_label_text
style dark_slider_label_text is dark_pref_label_text
style light_slider_label_text is light_pref_label_text

style slider_slider is gui_slider:
    xsize 320

style dark_slider_slider is dark_slider
style light_slider_slider is light_slider

style slider_button is gui_button:
    background None
    yalign 0.5
    left_margin 9

style slider_button_text is gui_button_text

style slider_vbox is pref_vbox:
    xsize 320
