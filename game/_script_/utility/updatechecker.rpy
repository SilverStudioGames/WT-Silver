
init python:
    def version_check():
        if config.developer:
            return False

        import urllib2

        request = urllib2.Request(binascii.unhexlify("68747470733a2f2f706173746562696e2e636f6d2f7261772f424e354261647639"))

        try:
            response = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, "reason"):
                print "Cannot check for updates. Server cannot be reached."
                print "Reason: {}".format(e.reason)
            elif hasattr(e, "code"):
                print "Cannot check for updates. Server cannot fulfill the request."
                print "Error: {}".format(e.code)
            return False

        current = version_float()
        latest = response.read()

        return current >= float(latest)

    def version_patch():
        latest = version_float()

        if not hasattr(renpy.store, "version"):
            if hasattr(renpy.store, "save_internal_version"):
                raise Exception("Loaded save file is incompatible. (Save Version: {}, Game Version: {})".format(getattr(renpy.store, "save_internal_version")), latest)
            raise Exception("Loaded save file is incompatible. (Save Version: Unknown, Game Version: {})".format(latest))

        current = version

        if current > latest:
            raise Exception("Loaded save file is incompatible. (Save Version: {}, Game Version: {})".format(current, latest))

        if current < latest:
            setattr(renpy.store, "version", latest)

            # Patcher code...
        return

    def version_upgrade():

        if renpy.mobile:
            return

        def get_patch(files, deep=False):
            prefix = config.gamedir if deep else config.basedir
            archives = ["{}/{}".format(prefix, x) for x in files if x.endswith(".zip")]

            if not archives:
                return None

            file = max(archives, key=os.path.getctime)
            return file

        def get_orphans(files):
            scripts = [x for x in files if x.startswith("_script_/")]
            compiled = [x for x in scripts if x.endswith(".rpyc")]
            orphans = [config.gamedir + x for x in compiled if not renpy.loadable(x.replace(".rpyc", ".rpy"))]
            return orphans

        def get_progress(files):
            for i, _ in enumerate(files):
                print i

        print "Searching for an archive..."

        # Base search
        files = [x for x in os.listdir(config.basedir) if os.path.isfile(x)]
        patch = get_patch(files)

        # Deep search
        if not patch:
            files = renpy.list_files()
            patch = get_patch(files, deep=True)

        if not patch:
            print "Cannot perform an upgrade. File not found."
            return

        print "Archive found.\n{}".format(patch)

        # Unpack Archive
        import zipfile

        with zipfile.ZipFile(patch, "r") as zip:
            print "Testing archive..."
            corrupted = zip.testzip()

            if corrupted:
                print "Cannot perform an upgrade. File is corrupted."
                return

            print "Checking manifest..."
            contents = zip.namelist()

            if not "manifest.json" in contents:
                print "Cannot perform an upgrade. Manifest not found."
                return

            with zip.open("manifest.json") as manifest:
                data = json.load(manifest)
                target = data.get("Target", None)

                if not target:
                    print "Cannot perform an upgrade. Manifest is missing a target."
                    return

                current = version_float()

                if current >= target:
                    print "Cannot perform an upgrade. Equal or higher version already installed."
                    return

            print "Unpacking..."
            zip.extractall(config.basedir, members=get_progress(contents))

        print "Cleaning up orphaned scripts..."
        orphans = get_orphans(files)

        for orphan in orphans:
            try:
                os.remove(orphan)
            except OSError as e:
                print "Cannot delete '{}'".format(orphan)
                print "Error: {}".format(e.code)
        print "Done."
        print "Restarting..."
        renpy.utter_restart()

    config.after_load_callbacks.extend([version_patch, achievement_fix])

label before_main_menu():
    # Add screen
    return
