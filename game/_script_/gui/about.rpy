## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

init offset = -1

# Not in use
screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix gui.theme("about")

        vbox:
            spacing gui.pref_spacing

            if config.window_title:
                label "[config.window_title]"
            else:
                label "[config.name!t]"
            #text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") size 12


style about_label is gui_label
style about_label_text is gui_label_text
style dark_about_label_text is dark_label_text
style light_about_label_text is light_label_text

style about_text is gui_text
style dark_about_text is dark_gui_text
style light_about_text is light_gui_text

style smallcredits is about_text:
    color '#000'
    size 14
    kerning 0.7

style about_name is about_text:
    font gui.bold_font
    color "#f9a001"
    outlines [(2, "#000", 0, 0)]

define gui.about = """{b}Witch Trainer: Silver{/b} is a complete rework of the popular game known as Witch Trainer.

The mod is developed by {a=https://www.silverstudiogames.com/}Silver Studio Games{/a} -- a group of people from around the world who work on this project in their free time."""
