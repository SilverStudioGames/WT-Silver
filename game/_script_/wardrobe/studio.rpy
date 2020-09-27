default studio.bg = 0
default studio.bg_hue = 0
default studio.bg_saturation = 1.0
default studio.bg_brightness = 0.0
default studio.bg_blur = 0.0
define studio.bg_list = ["wall_day", "castle", "forest", "highlight", "versus", "corridor", "custom"]

default studio.ov = 0
default studio.ov_alpha = 1.0
default studio.ov_hue = 0
default studio.ov_saturation = 1.0
default studio.ov_brightness = 0.0
default studio.ov_blur = 0.0
define studio.ov_list = [None, "curtains", "card", "g_bottom", "g_left", "g_circular"]

default studio.eyebrows = 0
default studio.eyes = 0
default studio.pupils = 0
default studio.mouth = 0
default studio.cheeks = 0
default studio.tears = 0
default studio.zoom = 0.5
default studio.flip = 1
default studio.alpha = 1.0

default studio.faces = None

init python in studio:
    def get_faces():
        filters = ("_mask", "_skin")
        d = {}

        for i in ("hermione", "tonks", "cho", "luna", "astoria", "susan"):
            d[i] = {}
            for j in ("eyebrows", "eyes", "mouth", "pupils", "cheeks", "tears"):
                path = "{}/characters/{}/face/{}/".format(renpy.config.gamedir, i, j)
                d[i][j] = [x.rsplit(".webp")[0] for x in renpy.os.listdir(path) if x.endswith(".webp") and not any(f in x for f in filters)]

                if j in ("cheeks", "tears"):
                    d[i][j].insert(0, None)

        return d

    def get_face(char):
        d = {
            "eyebrows": faces[char]["eyebrows"][eyebrows],
            "eyes": faces[char]["eyes"][eyes],
            "mouth": faces[char]["mouth"][mouth],
            "pupils": faces[char]["pupils"][pupils],
            "cheeks": faces[char]["cheeks"][cheeks],
            "tears": faces[char]["tears"][tears],
        }
        return d

label studio(char):

    # TODO: Finish adding support for multiple characters
    # Add presets saving.
    # Add character drag offset based on zoom.

    python:
        if not studio.faces:
            studio.faces = studio.get_faces()

            studio.eyebrows = studio.faces[char]["eyebrows"].index("base")
            studio.eyes = studio.faces[char]["eyes"].index("base")
            studio.mouth = studio.faces[char]["mouth"].index("base")
            studio.pupils = studio.faces[char]["pupils"].index("mid")
            studio.cheeks = studio.faces[char]["cheeks"].index(None)
            studio.tears = studio.faces[char]["tears"].index(None)

        last_char = char_active
        last_face = last_char.get_face()
        last_char.set_face(**studio.get_face(char))

    call screen studio

    python:
        if _return == "confirm":
            renpy.show_screen("studio")
            _filename = renpy.input("Filename", "exported", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#& ", length=64)
            renpy.pause(0.1, hard=True)
            item_to_export.export_data(True, _filename)
        else: # Close
            char_active = last_char
            char_active.set_face(**last_face)
    return

screen studio():
    tag studio
    zorder 30

    default visible = True

    key hkey_hide action ToggleScreenVariable("visible", True, False)
    key hkey_mhide action ToggleScreenVariable("visible", True, False)

    # TODO: Figure out why some values update live and some don't. (bg_image = works, hue, sat, bri = doesn't work)
    # Note: Defaults don't update at all (static?)

    $ bg_hue = HueMatrix(studio.bg_hue)
    $ bg_saturation = SaturationMatrix(studio.bg_saturation)
    $ bg_brightness = BrightnessMatrix(studio.bg_brightness)
    $ bg_image = "images/rooms/_bg_/{}.webp".format(studio.bg_list[studio.bg])
    $ bg = Transform(bg_image, matrixcolor=bg_hue*bg_saturation*bg_brightness, blur=studio.bg_blur)

    $ ov_hue = HueMatrix(studio.ov_hue)
    $ ov_saturation = SaturationMatrix(studio.ov_saturation)
    $ ov_brightness = BrightnessMatrix(studio.ov_brightness)
    $ ov_blur = studio.ov_blur
    $ ov_image = "images/rooms/overlays/{}.webp".format(studio.ov_list[studio.ov])
    $ ov = Transform(ov_image, matrixcolor=ov_hue*ov_saturation*ov_brightness, blur=ov_blur, alpha=studio.ov_alpha) if studio.ov_list[studio.ov] else None

    $ char_img = Flatten(char_active.get_image())
    $ char = Transform(char_img, zoom=studio.zoom, xzoom=studio.flip, alpha=studio.alpha)

    add bg

    drag:
        draggable visible
        drag_offscreen True
        anchor (0.6, 1.0)
        align (0.5, 1.0)
        child char

    add ov

    if visible:
        use close_button
        use studio_interface

screen studio_interface():

    style_prefix "studio"

    default eyebrows = studio.faces[active_girl]["eyebrows"]
    default eyes = studio.faces[active_girl]["eyes"]
    default pupils = studio.faces[active_girl]["pupils"]
    default mouth = studio.faces[active_girl]["mouth"]
    default cheeks = studio.faces[active_girl]["cheeks"]
    default tears = studio.faces[active_girl]["tears"]

    if export_in_progress:
        add "images/rooms/overlays/card_sp.webp"
        hbox:
            align (1.0, 1.0)
            textbutton "Confirm" action Return("confirm")
            textbutton "Cancel" action Return("cancel")
        fixed:
            style_prefix "studio_export"
            ypos 512

            text "WT:S [title_version]"
            if item_to_export.is_modded():
                text "Modded" size 12 color "#00b200" outlines [(1, "#000000", 0, 0)] xpos 392

    hbox:
        pos (25, 25)

        vbox:
            label "Character"
            bar value FieldValue(studio, "eyebrows", len(eyebrows)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character eyebrows"
            bar value FieldValue(studio, "eyes", len(eyes)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character eyes"
            bar value FieldValue(studio, "pupils", len(pupils)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character pupils"
            bar value FieldValue(studio, "mouth", len(mouth)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character mouth"
            bar value FieldValue(studio, "cheeks", len(cheeks)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character cheeks"
            bar value FieldValue(studio, "tears", len(tears)-1, False, step=1, force_step=True, action=Function(char_active.set_face, **studio.get_face(active_girl))) tooltip "Character tears"
            bar value FieldValue(studio, "zoom", 1.0, False, step=0.1, force_step=True) tooltip "Character Scale [studio.zoom]"
            bar value FieldValue(studio, "alpha", 1.0, False, step=0.1, force_step=True) tooltip "Character Opacity [studio.alpha]"

            textbutton "Flip" action ToggleVariable("studio.flip", -1, 1)

        vbox:
            label "Background"
            bar value FieldValue(studio, "bg", len(studio.bg_list)-1, False, step=1, force_step=True) tooltip "Background Image"
            bar value FieldValue(studio, "bg_hue", 360.0, False, step=1.0, force_step=True) tooltip "Background Hue [studio.bg_hue]"
            bar value FieldValue(studio, "bg_saturation", 1.0, False, step=0.1, force_step=False) tooltip "Background Saturation [studio.bg_saturation]"
            bar value FieldValue(studio, "bg_brightness", 1.0, False, step=0.1, force_step=False) tooltip "Background Brightness [studio.bg_brightness]"
            bar value FieldValue(studio, "bg_blur", 50.0, False, step=1.0, force_step=True) tooltip "Background Blur [studio.bg_blur]"

        vbox:
            label "Overlay"
            bar value FieldValue(studio, "ov", len(studio.ov_list)-1, False, step=1, force_step=True) tooltip "Overlay Image"
            bar value FieldValue(studio, "ov_hue", 360.0, False, step=1.0, force_step=True) tooltip "Overlay Hue [studio.ov_hue]"
            bar value FieldValue(studio, "ov_saturation", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Saturation [studio.ov_saturation]"
            bar value FieldValue(studio, "ov_brightness", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Brightness [studio.ov_brightness]"
            bar value FieldValue(studio, "ov_blur", 50.0, False, step=1.0, force_step=True) tooltip "Overlay Blur [studio.ov_blur]"
            bar value FieldValue(studio, "ov_alpha", 1.0, False, step=0.1, force_step=True) tooltip "Overlay Opacity [studio.ov_alpha]"

style studio_hbox:
    spacing 25

style studio_label_text:
    color "#f9d592"
    outlines [ (2, "#00000080", 0, 0) ]

style studio_bar:
    xsize 112
    xalign 0.5

style studio_button:
    xsize 106
    xalign 0.5

style studio_button_text:
    size 12

style studio_export_text:
    size 12
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    xanchor 1.0
    xpos 688
