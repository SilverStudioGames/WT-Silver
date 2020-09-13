
init python early:
    if renpy.version_tuple < (7,4,0,733):
        raise RuntimeWarning("Your Ren'Py launcher is outdated, the current minimal requirement is 7.4.0.733+\nPlease perform an update and try launching the game again.")

init python:
    if not config.developer:
        config.missing_image_callback = missing_image_func
        config.missing_label_callback = missing_label_func
    else:
        config.lint_hooks.append(lint_char_main_calls)
        renpy.arguments.register_command("whitespace", save_whitespace)

    if not renpy.android:
        config.start_interact_callbacks.append(fix_intel_renderer)

init -1 python:

    def missing_image_func(path):
        global systemerror
        systemerror = ["Missing image", path]
        return Image("images/blank.webp")


    def missing_label_func(name):
        global systemerror
        systemerror = ["Missing label", name]
        return "missing_label"


    def TBA_message(msg="Currently unavailable, check in later versions of the game."):
        renpy.show_screen("blktone5")
        renpy.with_statement(d3)
        renpy.say(sil, msg)
        renpy.hide_screen("blktone5")
        renpy.with_statement(d3)
        return


    def lint_char_main_calls():
        """
        Checks character calls that use the doll system.
        """
        renpy.execute_default_statement(False)
        char_lookup = {
            "ast_main": astoria,
            "cho_main": cho,
            "her_main": hermione,
            "ton_main": tonks
        }

        calls = [i for i in renpy.game.script.all_stmts if isinstance(i, renpy.ast.Call) and i.label in char_lookup]
        calls.sort(key=lambda i: (i.filename, i.linenumber))

        for c in calls:
            named_args = {}
            try:
                args, kwargs = c.arguments.evaluate(renpy.store.__dict__)
                node = renpy.game.script.lookup(c.label)
                named_args = node.parameters.apply(args, kwargs)
            except NameError:
                continue # Linting with undefined variables is difficult
            except Exception as e:
                print
                print "{}:{} {}".format(c.filename, c.linenumber, e)
                continue

            if named_args["face"] is not None:
                pass # Linting random face expressions is difficult

            char = char_lookup[c.label]

            # Reset face to default first, to avoid persisting errors from previous calls
            char.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
            char.set_face(
                mouth=named_args["mouth"],
                eyes=named_args["eyes"],
                eyebrows=named_args["eyebrows"],
                pupils=named_args["pupils"],
                cheeks=named_args["cheeks"],
                tears=named_args["tears"],
            )
            img = char.get_image()
            what = "Call to {}".format(c.label)
            renpy.lint.report_node = c
            renpy.lint.check_displayable(what, img)


    def save_whitespace(refresh=False):
        """
        Generates a whitespace information file.
        """
        global whitespace_dict

        ap = renpy.arguments.ArgumentParser("Generates a whitespace information file.", require_command=False)
        ap.add_argument("--refresh", action="store_true", help="Recalculate for all images.")
        args = ap.parse_args()
        if args.refresh or refresh:
            whitespace_dict = {}

        path = posixpath.join(config.basedir, "game")
        imgs = []
        for root, dirs, files in system.walk(path):
            for file in fnmatch.filter(files, "*.webp"):
                img = posixpath.join(root, file).split("/game/")[1]
                imgs.append(img)

        c = len(imgs)
        for i, img in enumerate(imgs):
            sys.stdout.write("\rCalculating whitespace... {:3.0f}%".format(i / float(c - 1) * 100.0))
            sys.stdout.flush()
            crop_whitespace(img)

        file = config.basedir + "/game/images.whitespace"
        with open(file, "w") as f:
            for img, box in sorted(whitespace_dict.iteritems()):
                f.write("{}:{},{},{},{}\n".format(img, *box))

        print "\rCalculating whitespace... Done!"
        return False


    def fix_intel_renderer():
        # Called only once per session
        config.start_interact_callbacks.remove(fix_intel_renderer)

        if renpy.windows and renpy.game.preferences.renderer == "auto":
            intel_detected = False

            if renpy.display.log.file:
                with open(renpy.display.log.file.name, "r") as file:
                    for line in file:
                        if line.startswith("Vendor:"):
                            intel_detected = "intel" in line.lower()
                            break

            if intel_detected:
                # Switch to Angle renderer
                renpy.game.preferences.renderer = "angle"
                renpy.display.draw.quit()
                renpy.display.draw = None
                renpy.display.interface.set_mode()


label missing_label():
    $ renpy.choice_for_skipping()
    $ err_msg1 = systemerror[0]
    $ err_msg2 = systemerror[1]
    if not mods_enabled:
        "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a bug. Don't worry, we will try to return you back to the office after displaying the error message, your save file won't be affected."
        "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} [err_msg1] '{color=#7a0000}[err_msg2]{/color}'\n\n\n{size=-4}You can report this bug on our {a=https://discord.gg/7PD57yt}discord{/a}.{/size}"
    else:
        "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a bug. Don't worry, we will try to return you back to the office after displaying the error message."
        "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} [err_msg1] '{color=#7a0000}[err_msg2]{/color}'\n\n\n{size=-4}If the issue persists, please delete all mods and try again.{/size}"
    if active_girl:
        $ active_girl = None
    $ systemerror = [None, None]
    jump main_room

screen placeholder():
    tag cg
    zorder 16 # above dolls

    add Placeholder("bg")
    add Placeholder("girl")


init 2000 python hide:
    def set_screen_layer(layer, *screens):
        for scr_name in screens:
            for _, scr in renpy.display.screen.get_all_screen_variants(scr_name):
                scr.layer = layer

    set_screen_layer("interface", "_performance", "_image_load_log")
