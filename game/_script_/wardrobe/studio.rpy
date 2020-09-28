default studio.faces = None
default studio.choices = None
default studio.drags = None

init python in studio:
    Transform = renpy.store.Transform
    Flatten = renpy.store.Flatten
    Drag = renpy.store.Drag

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

    def get_choices():
        d = {}

        for i in ("hermione", "tonks", "cho", "luna", "astoria", "susan"):
            d[i] = {}
            d[i]["eyebrows"] = faces[i]["eyebrows"].index("base")
            d[i]["eyes"] = faces[i]["eyes"].index("base")
            d[i]["mouth"] = faces[i]["mouth"].index("base")
            d[i]["pupils"] = faces[i]["pupils"].index("mid")
            d[i]["cheeks"] = faces[i]["cheeks"].index(None)
            d[i]["tears"] = faces[i]["tears"].index(None)
            d[i]["zoom"] = 0.5
            d[i]["flip"] = 1
            d[i]["alpha"] = 1.0

        d["background"] = {
            "image": 0,
            "alpha": 1.0,
            "hue": 0,
            "saturation": 1.0,
            "brightness": 0.0,
            "blur": 0.0,
            "list": ["wall_day", "castle", "forest", "highlight", "versus", "corridor", "custom"]
        }

        d["overlay"] = {
            "image": 0,
            "alpha": 1.0,
            "hue": 0,
            "saturation": 1.0,
            "brightness": 0.0,
            "blur": 0.0,
            "list": [None, "curtains", "card", "g_bottom", "g_left", "g_circular"]
        }
        return d

    def get_drags():
        active_girl = renpy.store.active_girl
        d = {}

        for i in ("hermione", "tonks", "cho", "luna", "astoria", "susan"):
            d[i] = [drag_init(getattr(renpy.store, i)), (i == active_girl)]
        return d

    def get_face(char):
        eyebrows = choices[char]["eyebrows"]
        eyes = choices[char]["eyes"]
        mouth = choices[char]["mouth"]
        pupils = choices[char]["pupils"]
        cheeks = choices[char]["cheeks"]
        tears = choices[char]["tears"]

        d = {
            "eyebrows": faces[char]["eyebrows"][eyebrows],
            "eyes": faces[char]["eyes"][eyes],
            "mouth": faces[char]["mouth"][mouth],
            "pupils": faces[char]["pupils"][pupils],
            "cheeks": faces[char]["cheeks"][cheeks],
            "tears": faces[char]["tears"][tears],
        }
        return d

    def drag_init(obj):
        char_obj = obj
        char_name = char_obj.name

        d = Transform(Flatten(char_obj.get_image()), zoom=choices[char_name]["zoom"], xzoom=choices[char_name]["flip"], alpha=choices[char_name]["alpha"])
        pos = (250, 0)

        drag = Drag(d, activated=drag_activated, drag_offscreen=True)
        drag.char_obj = char_obj
        drag.char_name = char_name
        drag.initial_pos = pos
        drag.style.pos = pos

        return drag

    def drag_activated(drag):
        drag = drag[0]

        renpy.store.char_active = drag.char_obj
        renpy.store.active_girl = drag.char_name

        drag.top()
        return

    def drag_update(drag):
        drag.char_obj.set_face(**get_face(drag.char_name))

        zoom = choices[drag.char_name]["zoom"]
        flip = choices[drag.char_name]["flip"]
        alpha = choices[drag.char_name]["alpha"]

        d = Flatten(drag.char_obj.get_image())
        d = Transform(d, zoom=zoom, xzoom=flip, alpha=alpha)
        drag.set_child(d)
        return

    def drag_reset(drag):
        choices[drag.char_name]["eyebrows"] = faces[drag.char_name]["eyebrows"].index("base")
        choices[drag.char_name]["eyes"] = faces[drag.char_name]["eyes"].index("base")
        choices[drag.char_name]["mouth"] = faces[drag.char_name]["mouth"].index("base")
        choices[drag.char_name]["pupils"] = faces[drag.char_name]["pupils"].index("mid")
        choices[drag.char_name]["cheeks"] = faces[drag.char_name]["cheeks"].index(None)
        choices[drag.char_name]["tears"] = faces[drag.char_name]["tears"].index(None)
        choices[drag.char_name]["zoom"] = 0.5
        choices[drag.char_name]["flip"] = 1
        choices[drag.char_name]["alpha"] = 1.0

        drag.char_obj.set_face(**get_face(drag.char_name))

        x, y = drag.initial_pos
        drag.snap(x, y, 0)

        drag_update(drag)
        return

label studio(char):

    # TODO: Finish adding presets saving.
    # Add character drag offset based on zoom.
    # Bugfixes

    python:
        if not studio.faces:
            studio.faces = studio.get_faces()
            studio.choices = studio.get_choices()
            studio.drags = studio.get_drags()

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
            active_girl = last_char.name
    return

screen studio():
    tag studio
    zorder 30
    style_prefix "studio"

    default visible = True

    key hkey_hide action ToggleScreenVariable("visible", True, False)
    key hkey_mhide action ToggleScreenVariable("visible", True, False)

    $ bg_hue = HueMatrix(studio.choices["background"]["hue"])
    $ bg_saturation = SaturationMatrix(studio.choices["background"]["saturation"])
    $ bg_brightness = BrightnessMatrix(studio.choices["background"]["brightness"])
    $ bg_blur = studio.choices["background"]["blur"]
    $ bg_matrix = bg_hue*bg_saturation*bg_brightness
    $ bg_image = studio.choices["background"]["list"][studio.choices["background"]["image"]]
    $ bg_image = "images/rooms/_bg_/{}.webp".format(bg_image)
    $ bg = Transform(bg_image, matrixcolor=bg_matrix, blur=bg_blur)

    $ ov_hue = HueMatrix(studio.choices["overlay"]["hue"])
    $ ov_saturation = SaturationMatrix(studio.choices["overlay"]["saturation"])
    $ ov_brightness = BrightnessMatrix(studio.choices["overlay"]["brightness"])
    $ ov_blur = studio.choices["overlay"]["blur"]
    $ ov_alpha = studio.choices["background"]["alpha"]
    $ ov_matrix = ov_hue*ov_saturation*ov_brightness
    $ ov_image = studio.choices["overlay"]["list"][studio.choices["overlay"]["image"]]

    if not ov_image is None:
        $ ov_image = "images/rooms/overlays/{}.webp".format(ov_image)
        $ ov = Transform(ov_image, matrixcolor=ov_matrix, blur=ov_blur, alpha=ov_alpha)
    else:
        $ ov = None

    $ active_drag = studio.drags[active_girl][0]

    add bg

    draggroup:
        for i in studio.drags.itervalues():
            if i[1]:
                add i[0]

    add ov

    if visible:
        use close_button

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
                $ drag_update = Function(studio.drag_update, active_drag)
                $ drag_reset = Function(studio.drag_reset, active_drag)

                bar value DictValue(studio.choices[active_girl], "eyebrows", len(studio.faces[active_girl]["eyebrows"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character eyebrows"
                bar value DictValue(studio.choices[active_girl], "eyes", len(studio.faces[active_girl]["eyes"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character eyes"
                bar value DictValue(studio.choices[active_girl], "pupils", len(studio.faces[active_girl]["pupils"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character pupils"
                bar value DictValue(studio.choices[active_girl], "mouth", len(studio.faces[active_girl]["mouth"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character mouth"
                bar value DictValue(studio.choices[active_girl], "cheeks", len(studio.faces[active_girl]["cheeks"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character cheeks"
                bar value DictValue(studio.choices[active_girl], "tears", len(studio.faces[active_girl]["tears"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character tears"
                bar value DictValue(studio.choices[active_girl], "zoom", 1.0, False, step=0.1, force_step=True, action=drag_update) tooltip "Character Scale"
                bar value DictValue(studio.choices[active_girl], "alpha", 1.0, False, step=0.1, force_step=True, action=drag_update) tooltip "Character Opacity"

                textbutton "Flip" action [ToggleDict(studio.choices[active_girl], "flip", -1, 1), drag_update]
                textbutton "Reset" action drag_reset

            vbox:
                label "Background"
                default bg_dict = studio.choices["background"]
                bar value DictValue(bg_dict, "image", len(bg_dict["list"])-1, False, step=1, force_step=True) tooltip "Background Image"
                bar value DictValue(bg_dict, "hue", 360.0, False, step=1.0, force_step=True) tooltip "Background Hue"
                bar value DictValue(bg_dict, "saturation", 1.0, False, step=0.1, force_step=False) tooltip "Background Saturation"
                bar value DictValue(bg_dict, "brightness", 1.0, False, step=0.1, force_step=False) tooltip "Background Brightness"
                bar value DictValue(bg_dict, "blur", 50.0, False, step=1.0, force_step=True) tooltip "Background Blur"

            vbox:
                label "Overlay"
                default ov_dict = studio.choices["overlay"]
                bar value DictValue(ov_dict, "image", len(ov_dict["list"])-1, False, step=1, force_step=True) tooltip "Overlay Image"
                bar value DictValue(ov_dict, "hue", 360.0, False, step=1.0, force_step=True) tooltip "Overlay Hue"
                bar value DictValue(ov_dict, "saturation", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Saturation"
                bar value DictValue(ov_dict, "brightness", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Brightness"
                bar value DictValue(ov_dict, "blur", 50.0, False, step=1.0, force_step=True) tooltip "Overlay Blur"
                bar value DictValue(ov_dict, "alpha", 1.0, False, step=0.1, force_step=True) tooltip "Overlay Opacity"

            hbox:
                style_prefix "studio_characters"

                for k, v in studio.drags.iteritems():
                    textbutton k action [ SelectedIf(v[1]), ToggleDict(studio.drags[k], 1, True, False), Function(studio.drag_activated, [v[0]]) ]

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

style studio_characters_button_text:
    size 10
    color "#f9d592"
    outlines [ (2, "#00000080", 0, 0) ]
