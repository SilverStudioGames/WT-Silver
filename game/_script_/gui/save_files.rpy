#
# Load/save screens
#
# These screens are responsible for letting the player save the game and load
# it again. Since they share nearly everything in common, both are implemented
# in terms of a third screen, file_slots.
#
# https://www.renpy.org/doc/html/screen_special.html#save
# https://www.renpy.org/doc/html/screen_special.html#load

init offset = -1

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    default page_modifier = 0

    use game_menu(title):

        fixed:

            # This ensures the input will get the enter event before any of the buttons do
            order_reverse True

            # The page name, which can be edited by clicking on a button
            button:
                style gui.theme("page_label")

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                hbox:
                    spacing 9
                    input:
                        style gui.theme("page_label_text")
                        value page_name_value

                    if page_name_value.editable:
                        text "{size=-4}{font=[gui.glyph_font]}✎{/font}{/size}"

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix gui.theme("slot")

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                transpose True

                for i in xrange(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)
                        sensitive ((FileCompatible(slot) and FileLoadable(slot)) if title == "Load" else True)

                        has fixed

                        if FileLoadable(slot):
                            add FileScreenshot(slot)

                            vbox:
                                style_prefix "slot_button"
                                xpos config.thumbnail_width
                                xsize gui.slot_width - config.thumbnail_width - gui.slot_height
                                yalign 0.5

                                if FileCompatible(slot):
                                    default slot_time_format = "{#file_time}%#d %B, %Y, %#H:%M" if renpy.windows else "{#file_time}%-d %B, %Y, %-H:%M"
                                    $ day = FileJson(slot, "day", missing="Unknown")
                                    $ playtime = FileJson(slot, "playtime", missing=0)
                                    $ minutes, seconds = divmod(int(playtime), 60)
                                    $ hours, minutes = divmod(minutes, 60)

                                    text FileTime(slot, format=_(slot_time_format))
                                    text "Day: {}".format(day)
                                    text "Playtime: {}H {}M {}S".format(hours, minutes, seconds)
                                else:
                                    text "NOT COMPATIBLE" color "#f00"

                            textbutton "{font=[gui.glyph_font]}✘{/font}":
                                style "slot_delete_button"
                                action FileDelete(slot, settings.get('confirm_delete'))

                            key "save_delete" action FileDelete(slot, settings.get('confirm_delete'))
                        else:
                            text "Empty Slot {}.".format(FileSlotName(slot, gui.file_slot_cols * gui.file_slot_rows)) style "slot_button_text"

            ## Buttons to access other pages.
            hbox:
                style_prefix gui.theme("page")

                align (0.5, 1.0)
                yoffset 8

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto") keysym "K_a"

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick") keysym "K_q"


                $ page_modifier = max(0, int(FilePageName(str(page_modifier+9), str(page_modifier+9)))-9)

                for page in xrange(1+page_modifier, 10+page_modifier):
                    textbutton "[page]":
                        xminimum 40
                        action FilePage(page)
                        if page < 10:
                            keysym "K_{}".format(page)

                textbutton _(">") action FilePageNext()

                key ["mousedown_4", "K_RIGHT", "repeat_K_RIGHT"] action FilePageNext()
                key ["mousedown_5", "K_LEFT", "repeat_K_LEFT"] action FilePagePrevious()


style page_label is gui_label

style page_label_text is gui_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style dark_page_label_text is dark_label_text:
    take page_label_text

style light_page_label_text is light_label_text:
    take page_label_text

style page_button is gui_button:
    background None
    padding (9, 4, 9, 4)

style page_button_text is gui_button_text:
    size 20
    xalign 0.5

style slot_button is gui_button:
    # background gui.muted_color
    xsize gui.slot_width
    ysize gui.slot_height+4
    padding (2, 2, 2, 2)

style dark_slot_button:
    take dark_gui_frame
    insensitive_background Fixed(Transform(Frame("gui/dark_frame.png", 8, 8)), "#00000040")

style light_slot_button:
    take light_gui_frame
    insensitive_background Fixed(Transform(Frame("gui/light_frame.png", 8, 8)), "#00000040")

style slot_button_text is gui_button_text:
    size 14
    xalign 0.5
    text_align 0.5
    idle_color gui.idle_small_color
    selected_idle_color gui.selected_color
    selected_hover_color gui.hover_color

style slot_delete_button is gui_button:
    background None
    idle_background None
    xsize gui.slot_height
    ysize gui.slot_height
    xalign 1.0

style slot_delete_button_text is slot_button_text:
    size 24
