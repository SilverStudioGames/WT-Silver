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

    use game_menu(title):

        fixed:

            # This ensures the input will get the enter event before any of the buttons do
            order_reverse True

            # The page name, which can be edited by clicking on a button
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                hbox:
                    spacing 9
                    input:
                        style "page_label_text"
                        value page_name_value

                    if page_name_value.editable:
                        text "{size=-4}{font=[gui.glyph_font]}✎{/font}{/size}":
                            at transform:
                                xzoom -1

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                transpose True

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has fixed

                        if FileLoadable(slot):
                            add FileScreenshot(slot) pos (0, 0) size (config.thumbnail_width, config.thumbnail_height)
                        else:
                            add Solid("#000") pos (0, 0) size (config.thumbnail_width, config.thumbnail_height)

                        fixed:
                            at transform:
                                alpha 0.3
                            pos (0, 0)
                            xysize (config.thumbnail_width, config.thumbnail_height)
                            text FileSlotName(slot, gui.file_slot_cols * gui.file_slot_rows) align (0.5, 0.5)

                        vbox:
                            xpos config.thumbnail_width
                            xsize gui.slot_width - config.thumbnail_width - gui.slot_height
                            yalign 0.5

                            # text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            text FileTime(slot, format=_("{#file_time}%B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                        if FileLoadable(slot):
                            textbutton "{font=[gui.glyph_font]}✘{/font}":
                                idle_background None
                                text_size 24
                                xsize gui.slot_height
                                xalign 1.0
                                action FileDelete(slot)

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label

style page_label_text is gui_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button is gui_button:
    background None
    padding (9, 4, 9, 4)

style page_button_text is gui_button_text

style slot_button is gui_button:
    background gui.muted_color
    xsize gui.slot_width
    ysize gui.slot_height
    padding (0, 0, 0, 0)

style slot_button_text is gui_button_text:
    size 14
    xalign 0.5
    idle_color gui.idle_small_color
    # selected_idle_color gui.selected_color
    selected_hover_color gui.hover_color

style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
