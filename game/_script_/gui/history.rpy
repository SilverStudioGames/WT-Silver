#
# History screen
#
# This is a screen that displays the dialogue history to the player. While
# there isn't anything special about this screen, it does have to access the
# dialogue history stored in _history_list.
#
# https://www.renpy.org/doc/html/history.html

init offset = -1

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix gui.theme("history")

        has vbox
        spacing 12

        default last_who = None

        # Group consecutive entries by same character (convert to list to avoid multiple enumeration problems)
        default groups = [(k, list(g)) for k, g in itertools.groupby(_history_list, key=lambda h: h.who or h.show_args.get("icon", None))]

        for k, g in groups:
            hbox:
                spacing 12

                $ g = list(g)
                if "icon" in g[0].show_args:
                    $ icon = g[0].show_args["icon"]
                    add Transform("interface/icons/head/{}.webp".format(icon), xzoom=-1) size (50, 50)
                elif g[0].who:
                    label g[0].who:
                        style "history_name"
                        substitute False

                        if "color" in g[0].who_args:
                            text_color g[0].who_args["color"]

                vbox:
                    spacing 6
                    for h in g:
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


# Tags that are allowed to be displayed on the history screen
define gui.history_allow_tags = ("number", "heart", "unicode")

# Height of a history screen entry, or None for variable height at the cost of performance
define gui.history_height = None #117

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window is empty:
    xfill True
    ysize gui.history_height
    padding (0,6)

style history_name:
    xanchor 1.0

style history_name_text:
    text_align 1.0

style history_text:
    text_align 0.0
    # layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

init 1 python:
    # Substitute variables when history is added
    def substitute_history_entry(h):
        if h.what:
            for p in history_match_tags:
                h.what = p.sub('{\g<1>=[\g<2>]}', h.what)

            h.what = renpy.substitute(h.what)

    config.history_callbacks.append(substitute_history_entry)

    # Match variables in tags and make them substitutable
    history_match_tags = []
    for t in gui.history_allow_tags:
        p = re.compile('\{(' + t + ')=([a-z_]+)\}', re.IGNORECASE)
        history_match_tags.append(p)
