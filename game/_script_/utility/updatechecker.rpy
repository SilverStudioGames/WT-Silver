
define update_available = check_for_updates()

init python:
    config.after_load_callbacks.append(update_savefile)

init -1 python:
    import urllib2

    def check_for_updates():
        if persistent.lastupdatechecktime == None:
            persistent.lastupdatechecktime = __import__('time').time()

        if persistent.lastupdatechecktime+86400.0 < __import__('time').time():
            updt_website = urllib2.Request(binascii.unhexlify("68747470733a2f2f706173746562696e2e636f6d2f7261772f424e354261647639"))
            try:
                updt_website2 = urllib2.urlopen(updt_website, timeout=5)
                version_check = updt_website2.read()
                return False if float(config.version) >= float(version_check) else True
            except:
                pass
        return False

    # Save compatibility patches
    def update_savefile():
        global save_internal_version

        try:
            if save_internal_version:
                pass
        except NameError:
            save_internal_version = 1.40

        # Apply update to old save
        achievement_fix()
