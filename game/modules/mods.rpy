init python:
    import json

    mods_enabled = False
    mods_list = {}

    def mods_module():
        global mods_enabled, mods_list
        _count = 0

        if renpy.loadable("mods/DISABLEMODS.txt"):
            return

        mods_enabled = True

        for dp, dn, fn in system.walk(config.basedir+"/game/mods/"):
            for i, mod in enumerate([f for f in fn if f.endswith(".rpym")]):
                _count += 1
                _path = system.path.join(dp, mod).replace("\\", "/").split("/game/")[1][:-5]
                _manifest = _path.split(mod[:-5])[0]+"manifest.json"

                if renpy.loadable(_manifest):
                    # Load JSON file
                    with open(config.basedir+"/game/"+_manifest) as fp:
                        _data = json.load(fp)
                    _name = _data["Name"]
                    mods_list[_name] = _data

                    # Load mod files
                    if float(mods_list[_name]["GameVer"]) >= float(compatible_version):
                        print "Found mod \"{}\" loading...".format(_name)
                        renpy.load_module(_path)
                    else:
                        _count -= 1
                        print "ERROR: Mod \"{}\" is outdated! Reported compatible game version {}, current game version {}".format(_name, mods_list[_name]["GameVer"], config.version)
                else:
                    _count -= 1
                    print "ERROR: Mod \"{}\" is missing manifest.json".format(str(dp))

        print "{} Mods Enabled".format(_count)
        return

    mods_module()

label splashscreen:
    if not mods_enabled:
        return

    call screen mods_warning with dissolve
    return

screen mods_warning():

    default bg = At("title/00.webp", gaussianblur(15.0))
    add bg

    text "!" size 300 color "#7a0000" ypos 2 xalign 0.5 outlines [(1, "#00000080", 1, 0)]
    frame:
        style "empty"
        align (0.5, 0.7)
        xsize 800
        text "Mods Warning" align (0.5, 0.46) size 40 color "#7a0000" outlines [(1, "#00000080", 1, 0)]
        text "Unofficial content has been detected in your game files. Mods are not officially supported and might cause unexpected behaviour. If you come across any issues please uninstall all mods." align (0.5, 0.58) color "#fff" outlines [(1, "#00000080", 1, 0)]
        textbutton "Got it.":
            align (0.5, 0.7)
            text_size 32
            action Return()
