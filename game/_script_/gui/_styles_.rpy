#
# Common styles
#

init offset = -1

style default:
    language 'unicode'
    font gui.bold_font
    color "#402313"
    size 16
    outline_scaling "linear"

style input:
    adjust_spacing False

style hyperlink_text:
    underline False
    hover_color "#4cf"
    idle_color "#08f"

style gui_text:
    font gui.text_font
    color "#000"

style dark_gui_text:
    color settings.get('text_color_night')

style light_gui_text:
    color settings.get('text_color_day')

style gui_button:
    padding (4, 4, 4, 4)
    background None

style gui_button_text is gui_text:
    yalign 0.5
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color

style label_text is gui_text:
    # font gui.bold_font
    color gui.accent_color

style dark_label_text is dark_gui_text:
    font gui.bold_font

style light_label_text is light_gui_text:
    font gui.bold_font

style prompt_text is gui_text

style bar:
    ysize gui.bar_size
    left_bar "bar_[prefix_]fill"
    right_bar "bar_[prefix_]empty"

style vbar:
    xsize gui.bar_size
    bottom_bar "bar_[prefix_]fill"
    top_bar "bar_[prefix_]empty"

style scrollbar:
    unscrollable gui.unscrollable
    ysize gui.scrollbar_size
    base_bar Frame("scrollbar_horizontal_[prefix_]bar", gui.slider_borders, tile=gui.slider_tile)
    thumb Frame("scrollbar_horizontal_[prefix_]thumb", gui.slider_borders, tile=gui.slider_tile)

style vscrollbar:
    unscrollable gui.unscrollable
    xsize gui.scrollbar_size
    base_bar Frame("scrollbar_vertical_[prefix_]bar", gui.slider_borders, tile=gui.slider_tile)
    thumb Frame("scrollbar_vertical_[prefix_]thumb", gui.slider_borders, tile=gui.slider_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame(Solid(gui.muted_color))
    thumb Frame("slider_horizontal_[prefix_]thumb", gui.slider_borders, tile=gui.slider_tile, xsize=gui.thumb_size)

style dark_slider:
    left_bar Frame("dark_slider_full", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("dark_slider_empty", gui.slider_borders, tile=gui.slider_tile)
    thumb Frame(Transform("gui/dark_frame.png", alpha=0.5), gui.slider_borders, tile=gui.slider_tile, xsize=gui.thumb_size)
    hover_thumb Frame("gui/dark_frame.png", gui.slider_borders, tile=gui.slider_tile, xsize=gui.thumb_size)

style light_slider:
    left_bar Frame("light_slider_full", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("light_slider_empty", gui.slider_borders, tile=gui.slider_tile)
    thumb Frame(Transform("gui/light_frame.png", alpha=0.5), gui.slider_borders, tile=gui.slider_tile, xsize=gui.thumb_size)
    hover_thumb Frame("gui/light_frame.png", gui.slider_borders, tile=gui.slider_tile, xsize=gui.thumb_size)

style vslider:
    xsize gui.slider_size
    base_bar Frame("slider_vertical_[prefix_]bar", gui.slider_borders, tile=gui.slider_tile)
    thumb "slider_vertical_[prefix_]thumb"

# Button

style imagemap:
    activate_sound "sounds/click3.mp3"

style button:
    activate_sound "sounds/click3.mp3"
    insensitive_background "#463b3be6"
    selected_background "#766a6ae6"
    padding (5, 5, 5, 5)

style dark_button:
    background "#5d5151e6"
    hover_background "#897e75"
    insensitive_background "#9e8449"

style light_button:
    background "#ac8d5ae6"
    hover_background "#97681f"
    insensitive_background "#d1a02eb3"

style button_text:
    hover_color "#fff"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#fff"
    outlines [(1, "#00000080", 1, 0)]

style dark_button_text:
    color "#9b8d84"

style light_button_text:
    color "#f9d592"

style dark_overlay_button is empty:
    hover_foreground "#7d75aa40"

style light_overlay_button is empty:
    hover_foreground "#e3ba7140"

style dark_overlay_button_text is dark_button_text
style light_overlay_button_text is light_button_text

# Frame

style frame:
    padding (4, 4, 4, 4)

style dark_frame is dark_gui_frame

style light_frame is light_gui_frame

style gui_frame:
    padding (6, 6, 6, 6)

style dark_gui_frame:
    background Transform(Frame("gui/dark_frame.png", 8, 8))

style light_gui_frame:
    background Transform(Frame("gui/light_frame.png", 8, 8))

# Tabs

style tab_hbox:
    spacing gui.pref_spacing
    margin (-6, -6)

style tab_button is gui_button:
    padding (12, 12)

style dark_tab_button:
    take dark_gui_frame

style light_tab_button:
    take light_gui_frame

style tab_button_text is gui_button_text

# Say label

style say_label is default:
    bold False
    text_align 0.5
    align (0.5, 0.5)
    outlines [(1, settings.get('text_outline'), 1, 0)]

style dark_say_label:
    color settings.get('text_color_night')

style light_say_label:
    color settings.get('text_color_day')

# Say dialogue

style say_dialogue is default:
    outlines [(1, settings.get('text_outline'), 1, 0)]

style dark_say_dialogue:
    color settings.get('text_color_night')

style light_say_dialogue:
    color settings.get('text_color_day')

style say_thought is say_dialogue
style dark_say_thought is dark_say_dialogue
style light_say_thought is light_say_dialogue

# Window

style window is gui_frame:
    xalign 0.5
    xfill True
    # yalign gui.textbox_yalign
    # ysize gui.textbox_height

style dark_window is dark_gui_frame:
    take window

style light_window is light_gui_frame:
    take window

# Say window

style say_window:
    ysize 143
    padding (250, 40, 250, 0)
    top_margin 22
    yalign 1.0

style dark_say_window is dark_window:
    take say_window
    background "interface/frames/gray/frame.webp"

style light_say_window is light_window:
    take say_window
    background "interface/frames/gold/frame.webp"

# Namebox

style namebox is gui_frame:
    xpadding 15
    pos (-15, -50)
    ysize 32
    xminimum 164
    text_align 0.5

style dark_namebox is dark_gui_frame:
    take namebox
    # background Transform(Frame("gui/dark_namebox.png", 8, 8))

style light_namebox is light_gui_frame:
    take namebox
    # background Transform(Frame("gui/light_namebox.png", 8, 8))

# Text

style dark_text:
    color settings.get('text_color_night')
    outlines [(1, settings.get('text_outline'), 1, 0)]

style light_text:
    color settings.get('text_color_day')
    outlines [(1, settings.get('text_outline'), 1, 0)]
