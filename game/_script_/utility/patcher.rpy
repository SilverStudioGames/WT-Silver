init python:
    import zipfile

    if not renpy.android:
        patchfn = os.path.join(config.basedir, "patch.zip")

    def semver(flat):
        vs = flat.split(".")
        major, minor, patch = vs[0], vs[1][:2], vs[1][2:] or "0"
        return tuple(map(int, [major, minor, patch]))

    def check_for_patch():
        if os.path.isfile(patchfn):
            versionr = re.compile(r'define config\.version = "([\d\.]+)"')
            with zipfile.ZipFile(patchfn, "r") as patchf:
                if "game/_script_/options.rpy" in patchf.namelist():
                    with patchf.open("game/_script_/options.rpy") as optionsf:
                        for line in optionsf:
                            m = versionr.search(line.decode("utf8"))
                            if m is not None:
                                patch_version = semver(m.group(1))
                                current_version = semver(config.version)
                                if patch_version[:2] == current_version[:2] and patch_version > current_version:
                                    return patch_version
        return None

    def apply_patch():
        with zipfile.ZipFile(patchfn, "r") as patchf:
            patchf.extractall(config.basedir)

    def run_patcher():
        patch_version = check_for_patch()
        if patch_version:
            renpy.run(Confirm(
                "A patch is ready to be installed. It will update the game to version {}.{}.{}.\nDo you want to install it now?".format(*patch_version),
                Call("apply_patch", patch_version)
            ))

label before_main_menu():
    if not renpy.android:
        $ run_patcher()
    return

label apply_patch(patch_version):
    show screen patcher(patch_version)
    with None
    $ apply_patch()
    pause 1
    call screen patcher(patch_version, done=True)
    with None
    $ renpy.quit(relaunch=True)
    return

screen patcher(patch_version, done=False):
    zorder 999
    modal True

    window:
        style "gm_root"

    frame:
        style_prefix "confirm"

        xfill True
        xmargin 50
        ypadding 25
        yalign .25

        vbox:
            xfill True
            spacing 25

            if done:
                text "The game has been updated to {}.{}.{} and will now restart.".format(*patch_version):
                    text_align 0.5
                    xalign 0.5
                    style "night_text"
                    color "#9b8d84"
                hbox:
                    spacing 100
                    xalign .5
                    textbutton _("Ok") action Return(True)
            else:
                text "Installing patch {}.{}.{}...".format(*patch_version):
                    text_align 0.5
                    xalign 0.5
                    style "night_text"
                    color "#9b8d84"
