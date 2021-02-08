default mods_enabled = set()
default mods_parsed = set()

init python:
    import json

    mods_list = {}

    def import_mods():
        global mods_enabled, mods_list

        mods = filter(lambda x: x.endswith(".json"), renpy.list_files())

        for i, manifest in enumerate(mods):
            path = os.path.split(manifest)[0]
            files = filter(lambda x: path in x, renpy.list_files())
            scripts = filter(lambda x: x.endswith(".rpym"), files)
            manifest = renpy.file(manifest)
            logo = "{}/logo.webp".format(path)

            if not renpy.loadable(logo):
                logo = "#000"

            # Read manifest
            with manifest as f:
                data = json.load(f)

            modname = data.get("Name", None)

            if not modname:
                continue

            mods_list[modname] = data
            mods_list[modname]["Files"] = files
            mods_list[modname]["Path"] = path
            mods_list[modname]["LoadOrder"] = i # TODO: Make load order customisable
            mods_list[modname]["Logo"] = logo

    def parse_mods():
        for mod in mods_list.itervalues():
            modname = mod["Name"]
            if not modname in mods_enabled or modname in mods_parsed:
                continue

            path = mod["Path"]

            for file in mod["Files"]:
                if not file.endswith(".rpym"):
                    continue

                filename = os.path.split(file)[1]
                fileobj = renpy.file(file)

                with fileobj as s:
                    data = s.read()

                renpy.load_string(data, "{}/{}".format(path, filename))

            mods_parsed.add(modname)
        return

    def toggle_mod(mod):
        global mods_enabled

        if not main_menu:
            renpy.notify("Mods can be enabled or disabled in the main menu only.")
            return

        if mod in mods_enabled:
            renpy.notify("Mod disabled.")
            mods_enabled.remove(mod)
        else:
            renpy.notify("Mod Enabled.")
            mods_enabled.add(mod)

    import_mods()
    config.after_load_callbacks.append(parse_mods)


