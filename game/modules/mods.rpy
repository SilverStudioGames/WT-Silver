default mods_enabled = set()
default mods_parsed = set()

init python:
    import json

    mods_list = {}

    def import_mods():
        global mods_enabled, mods_list

        all_files = renpy.list_files()

        if renpy.android:
            # Include files outside the application archive and strip the directory path.
            # Normally it wouldn't be necessary but `renpy.list_files` does not list files outside archives on android.
            for dir in config.searchpath:
                all_files.extend([os.path.join(path.replace(dir, ""), name) for path, _, files in os.walk(dir) for name in files])

        mods = filter(lambda x: x.endswith(".json"), all_files)

        for i, manifest in enumerate(mods):
            path = os.path.split(manifest)[0]
            files = filter(lambda x: path in x, all_files)
            scripts = filter(lambda x: x.endswith(".rpym"), files)
            logo = "{}/logo.webp".format(path)

            if not renpy.loadable(logo):
                logo = "#000"

            # Read manifest
            with renpy.file(manifest) as f:
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

                with renpy.file(file) as s:
                    data = s.read()

                # Note: load_string func breaks after utter restart (Bug?)
                renpy.load_string(data, "{}/{}".format(path, filename))

            mods_parsed.add(modname)
        return

    def toggle_mod(mod):
        if not main_menu:
            renpy.notify("Mods can be enabled or disabled in the main menu only.")
            return

        mods = getattr(renpy.store, "mods_enabled")

        if mod in mods:
            renpy.notify("Mod disabled.")
            mods.remove(mod)
        else:
            renpy.notify("Mod Enabled.")
            mods.add(mod)

    import_mods()
    config.after_load_callbacks.append(parse_mods)


