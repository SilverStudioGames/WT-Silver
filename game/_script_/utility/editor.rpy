init python:
    def catch_character_call(label, called):
        if called:
            if label.startswith(("her_main", "cho_main", "ast_main", "ton_main")):
                editor.catch(label)

    class ExpressionEditor(NoRollback):
        transitions = ("d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "flash", "flashbulb", "flashbb", "flashblood", "kissiris", "black_magic", "blackfade", "morph", "teleport", "vpunch_repeat", "hpunch", "vpunch", "pushleft", "dissolve", "slideawayright", "wipedown", "slidedown", "pixellate", "blinds", "squares", "slideup", "pushup", "slideleft", "pushright", "wiperight", "irisin", "wipeleft", "slideawayleft", "pushdown", "irisout", "slideawayup", "wipeup", "slideawaydown", "slideright", "move")

        transforms = ("move_fade", "sprite_fly_idle")

        char = {"her_main": "hermione",
                "ton_main": "tonks",
                "ast_main": "astoria",
                "cho_main": "cho"}

        def __init__(self):
            self.label = None
            self.line = None
            self.line_contents = None
            self.args = None

            self._file = None
            self._file_contents = None

            self.define_expressions()
            self.changes = _dict()

        def launch_editor(self, file=None, line=None):
            """Launches external text editor."""
            if renpy.in_rollback() or renpy.in_fixed_rollback():
                return

            renpy.launch_editor([file], line)
            return

        def overwrite_statement(self):
            if renpy.in_rollback() or renpy.in_fixed_rollback():
                return

            # Backup file contents
            with open(self._file, "r") as f:
                self._file_contents = f.readlines()

            try:
                new = self.get_new_statement()
                old = self.line_contents

                # Overwrite the file contents
                with open(self._file, "w") as f:
                    for n, l in enumerate(self._file_contents, 1):
                        if n == self.line:
                            f.writelines(l.replace(self.line_contents, new))
                            if n not in self.changes.get(self._file, _list()):
                                self.changes.setdefault(self._file, _dict()).setdefault(n, [old, new, self.args, self.char[self.label], None])
                            else:
                                self.changes[self._file][n] = [old, new, self.args, self.char[self.label], None]
                        else:
                            f.writelines(l)
            except:
                # Restore backup
                with open(self._file, "w") as f:
                    for l in self._file_contents:
                        f.writelines(l)
                renpy.notify("An error occurred, no changes were made.")
                return

            self.line_contents = new
            renpy.notify("Saved.")
            return

        def get_new_statement(self):
            text = "\"\", " if not self.args["text"] else "\"{}\", ".format(self.args["text"].replace("\"", "\\\""))

            mouth = "" if self.args["mouth"] == False else "\"{}\", ".format(self.args["mouth"])
            eyes = "" if self.args["eyes"] == False else "\"{}\", ".format(self.args["eyes"])
            eyebrows = "" if self.args["eyebrows"] == False else "\"{}\", ".format(self.args["eyebrows"])
            pupils = "" if self.args["pupils"] == False else "\"{}\", ".format(self.args["pupils"])
            hair = "" if self.label != "ton_main" or self.args["hair"] in (None, "(No change)") else "hair=\"{}\", ".format(self.args["hair"])

            cheeks = "" if self.args["cheeks"] in (None, "(No change)") else "cheeks=\"{}\", ".format(self.args["cheeks"])
            tears = "" if self.args["tears"] in (None, "(No change)") else "tears=\"{}\", ".format(self.args["tears"])
            emote = "" if self.args["emote"] == None else "emote=\"{}\", ".format(self.args["emote"])
            face = "" if self.args["face"] == None else "face=\"{}\", ".format(self.args["face"])

            xpos = self.args["xpos"]
            if xpos == None:
                xpos = ""
            else:
                xpos = "xpos={}, ".format(xpos) if is_integer(xpos) else "xpos=\"{}\", ".format(xpos)

            ypos = self.args["ypos"]
            if ypos == None:
                ypos = ""
            else:
                ypos = "ypos={}, ".format(ypos) if is_integer(ypos) else "ypos=\"{}\", ".format(ypos)

            flip = "" if self.args["flip"] == None else "flip={}, ".format(self.args["flip"])
            trans = "" if self.args["trans"] == None else "trans={}, ".format(self.args["trans"])
            animation = "" if self.args["animation"] == False else "animation={}".format(self.args["animation"])

            new = "call {}({}{}{}{}{}{}{}{}{}{}{}{}{}{}{})".format(self.label, text, mouth, eyes, eyebrows, pupils, hair, cheeks, tears, emote, face, xpos, ypos, flip, trans, animation)

            new = new.replace(", )", ")")
            return new

        def catch(self, label):
            # Get file and line number
            stack = renpy.get_return_stack()[-1]
            node = renpy.game.script.namemap.get(stack, None)

            # Console call fallback
            if node.filename == "<string>":
                return

            self._file = config.basedir+"/"+node.filename
            self.line = node.linenumber
            self.label = label


            if self.changes.get(self._file, _dict()).get(self.line, None):
                # Get arguments from cache
                self.args = self.changes[self._file][self.line][2]
            else:
                # Get arguments from node
                node = renpy.game.script.lookup_or_none(self.label)
                self.args = _dict([(k, getattr(store, k)) for k in node.parameters.apply(None, None).iterkeys()])

            if self.args["cheeks"] == None:
                self.args["cheeks"] = "(No change)"
            if self.args["tears"] == None:
                self.args["tears"] = "(No change)"
            if self.label == "ton_main":
                if self.args["hair"] == None:
                    self.args["hair"] = "(No change)"

            # Lookup transition name
            if self.args["trans"] != None:
                _transitions = _dict([(obj.callable, name) for (name, obj) in store.__dict__.iteritems() if name in self.transitions])
                self.args["trans"] = _transitions[self.args["trans"].callable]

            # Lookup transform name
            if not self.args["animation"] in (False, None):
                _transforms = _dict([(obj, name) for (name, obj) in store.__dict__.iteritems() if isinstance(obj, renpy.atl.ATLTransformBase)])
                self.args["animation"] = _transforms[self.args["animation"]]

            # Check for already made changes and hijack the line.
            if self.changes.get(self._file, _dict()).get(self.line, None):
                self.line_contents = self.changes[self._file][self.line][1]
            else:
                # Read file and find the line in question
                with open(self._file, "U") as f:
                    for n, l in enumerate(f, 1):
                        if n == self.line:
                            l = l.partition("#")[0].strip() # Ignore comments and strip spaces
                            if l.startswith("call {}".format(self.label)):
                                self.line_contents = l
                                break
            self.set_expressions
            return

        def set_data(self, arg, val):
            if renpy.in_rollback() or renpy.in_fixed_rollback():
                return

            self.args[arg] = val
            self.set_expressions()
            self.overwrite_statement()

        def get_tooltip(self, file, line):

            if self.changes[file][line][4] == None:
                imagepath = config.basedir.replace("\\", "/")
                args = self.changes[file][line][2]
                char = self.changes[file][line][3]

                if char == "hermione":
                    hair = her_hair_base
                    box = (450, 275, 320, 240)
                elif char == "tonks":
                    hair = ton_hair_base_new
                    box = (450, 275, 320, 240)
                elif char == "astoria":
                    hair = ast_hair_base
                    box = (450, 320, 280, 240)
                elif char == "cho":
                    hair = cho_hair_ponytail1
                    box = (450, 310, 280, 240)


                sprites = [imagepath+"/game/characters/"+char+"/body/base/front.webp"]

                if not "No change" in args["cheeks"]:
                    sprites.append(imagepath+"/game/characters/"+char+"/face/cheeks/"+args["cheeks"]+".webp")
                sprites.append(imagepath+"/game/characters/"+char+"/face/eyes/"+args["eyes"]+".webp")
                if not any(x in args["eyes"] for x in ("closed", "happyCl")):
                    m = imagepath+"/game/characters/"+char+"/face/eyes/"+args["eyes"]+"_mask.webp"
                    sprites.append(AlphaMask(imagepath+"/game/characters/"+char+"/face/pupils/"+args["pupils"]+".webp", m))
                sprites.append(imagepath+"/game/characters/"+char+"/face/eyebrows/"+args["eyebrows"]+".webp")
                if not "No change" in args["tears"]:
                    sprites.append(imagepath+"/game/characters/"+char+"/face/tears/"+args["tears"]+".webp")
                sprites.append(imagepath+"/game/characters/"+char+"/face/mouth/"+args["mouth"]+".webp")

                # Hair
                sprites.extend(hair.get_back())
                if hair.back_outline:
                    sprites.append(hair.back_outline)
                sprites.append(hair.get_image())

                sprites = tuple(itertools.chain.from_iterable(((0,0), x) for x in sprites))

                self.changes[file][line][4] =  At(Crop(box, Composite((1010, 1200), *sprites)), Transform(zoom=0.5))
            return self.changes[file][line][4]

        def set_expressions(self):
            c = getattr(renpy.store, self.char[self.label])

            cheeks = None if self.args["cheeks"] in (None, "(No change)") else self.args["cheeks"]
            tears = None if self.args["tears"] in (None, "(No change)") else self.args["tears"]

            if self.label == "ton_main":
                hair = None if self.args["hair"] in (None, "(No change)") else self.args["hair"]

                # Hardcoded for tonks
                if hair:
                    if hair in ("neutral", "basic", "reset"):
                        target_color = tonks_haircolor
                    elif hair in ("red", "angry", "furious"):
                        target_color = [[164, 34, 34, 255], [219, 83, 83, 255]]
                    elif hair in ("orange", "upset", "annoyed"):
                        target_color = [[228, 93, 34, 255], [246, 193, 170, 255]]
                    elif hair in ("yellow", "happy", "cheerful"):
                        target_color = [[255, 213, 23, 255], [255, 239, 167, 255]]
                    elif hair in ("green", "disgusted"):
                        target_color = [[111, 205, 75, 255], [200, 237, 186, 255]]
                    elif hair in ("blue", "sad"):
                        target_color = [[64, 75, 205, 255], [182, 186, 237, 255]]
                    elif hair in ("purple"):
                        target_color = [[205, 75, 205, 255], [237, 186, 237, 255]]
                    elif hair in ("white", "scared"):
                        target_color = [[238, 238, 241, 255], [249, 249, 250, 255]]
                    elif hair in ("pink", "horny"):
                        target_color = [[255, 105, 180, 255], [251, 205, 222, 255]]

                    tonks.get_equipped("hair").set_color(target_color)

            c.set_face(mouth=self.args["mouth"], eyes=self.args["eyes"], eyebrows=self.args["eyebrows"], pupils=self.args["pupils"], cheeks=cheeks, tears=tears)
            c.apply_transition()

        def get_expressions(self, type):
            return sorted(self.expressions[self.char[self.label]][type])

        def define_expressions(self):
            def scan_files(char):
                mouths = tuple(x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/mouth/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x)
                eyes = tuple(x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/eyes/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x)
                eyebrows = tuple(x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/eyebrows/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x)
                pupils = tuple(x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/pupils/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x)

                cheeks = ["(No change)"]
                tears = ["(No change)"]
                hair = ["(No change)", "neutral", "angry", "upset", "happy", "disgusted", "sad", "purple", "scared", "horny"]

                cheeks.extend([x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/cheeks/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x])
                tears.extend([x.rsplit(".webp")[0] for x in os.listdir(config.basedir+"/game/characters/"+char+"/face/tears/") if x.endswith(".webp") and not "_mask" in x and not "_skin" in x])

                return _dict([("mouths", mouths), ("eyes", eyes), ("eyebrows", eyebrows), ("pupils", pupils), ("cheeks", cheeks), ("tears", tears), ("hair", hair)])

            self.expressions = _dict([(x, scan_files(x)) for x in self.char.itervalues()])

    def editor_reset():
        editor.changes = _dict()

    if config.developer and not renpy.mobile:
        config.label_callback = catch_character_call
        config.after_load_callbacks.append(editor_reset)

        editor = ExpressionEditor()

screen editor():
    layer "interface"
    tag editor
    zorder 0

    default minimised = False
    default minimised_history = False
    default frame_size = (250, 450)

    if not _menu:

        # Editor
        drag:
            drag_name "editor"
            draggable True
            drag_offscreen False
            drag_handle (0, 0, 1.0, 26)
            pos (50, 50)
            frame:
                xysize (frame_size if not minimised else (250, 28))
                button action NullAction() style "empty" xysize (frame_size if not minimised else (250, 28)) ypos 18

                text "Expression Editor {size=-2}ver 0.2{/size}" size 10 color "#FFF" outlines [(1, "#00000080", 1, 0)]

                textbutton "_" ysize 28 offset (-32, -7) text_size 15 text_yalign 0.5 xalign 1.0 action [ToggleScreenVariable("minimised", True, False), SelectedIf(None)] tooltip ("Maximise" if minimised else "Minimise")
                textbutton "x" ysize 28 offset (6, -7) text_size 15 text_yalign 0.5 xalign 1.0 action Hide("editor") tooltip "Close editor"

                frame:
                    style "empty"
                    xysize (236, 2)
                    pos (0, 18)
                    background "#FFFFFF80"

                if not minimised:
                    if editor.label:
                        $ f = editor._file.split("/")[-1]
                        $ l = editor.line

                        textbutton "File: [f]\nLine: [l]" style "empty" text_size 10 text_color "#FFF" pos (0, 160) text_outlines [(1, "#00000080", 1, 0)] action Function(editor.launch_editor, editor._file, l)

                        textbutton "Reload" action Function(_reload_game) xanchor 1.0 align (1.0, 1.0)

                        if not False in (editor.args["pupils"], editor.args["eyebrows"], editor.args["eyes"], editor.args["mouth"]):
                            use dropdown_menu(name="Tears: "+str(editor.args["tears"]), pos=(0, 140), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("tears"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["tears"])), Function(editor.set_data, "tears", i)]
                            use dropdown_menu(name="Cheeks: "+str(editor.args["cheeks"]), pos=(0, 120), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("cheeks"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["cheeks"])), Function(editor.set_data, "cheeks", i)]
                            if editor.label == "ton_main":
                                use dropdown_menu(name="Hair: "+str(editor.args["hair"]), pos=(0, 100), items_offset=(0, 0), background="#FFFFFF80"):
                                    for i in editor.get_expressions("hair"):
                                        textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["hair"])), Function(editor.set_data, "hair", i)]
                            use dropdown_menu(name="Pupils: "+str(editor.args["pupils"]), pos=(0, 80), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("pupils"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["pupils"])), Function(editor.set_data, "pupils", i)]
                            use dropdown_menu(name="Eyebrows: "+str(editor.args["eyebrows"]), pos=(0, 60), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("eyebrows"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["eyebrows"])), Function(editor.set_data, "eyebrows", i)]
                            use dropdown_menu(name="Eyes: "+str(editor.args["eyes"]), pos=(0, 40), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("eyes"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["eyes"])), Function(editor.set_data, "eyes", i)]
                            use dropdown_menu(name="Mouth: "+str(editor.args["mouth"]), pos=(0, 20), items_offset=(0, 0), background="#FFFFFF80"):
                                for i in editor.get_expressions("mouths"):
                                    textbutton "[i]" text_size 10 action [SelectedIf(i==str(editor.args["mouth"])), Function(editor.set_data, "mouth", i)]
                        else:
                            text "This character line uses unrecognized expression and requires to be changed manually." size 10 color "#FFF" align (0.5, 0.5) outlines [(1, "#00000080", 1, 0)]
                    else:
                        text "Not applicable." size 15 color "#FFF" align (0.5, 0.5) outlines [(1, "#00000080", 1, 0)]

        # History
        drag:
            drag_name "editor_history"
            draggable True
            drag_offscreen False
            drag_handle (0, 0, 1.0, 26)
            pos (300, 50)
            frame:
                xysize (frame_size if not minimised_history else (250, 28))
                button action NullAction() style "empty" xysize (frame_size if not minimised_history else (250, 28)) ypos 18

                text "History" size 10 color "#FFF" outlines [(1, "#00000080", 1, 0)]

                textbutton "_" ysize 28 offset (-32, -7) text_size 15 text_yalign 0.5 xalign 1.0 action [ToggleScreenVariable("minimised_history", True, False), SelectedIf(None)] tooltip ("Maximise" if minimised_history else "Minimise")
                textbutton "x" ysize 28 offset (6, -7) text_size 15 text_yalign 0.5 xalign 1.0 action Hide("editor") tooltip "Close editor"

                frame:
                    style "empty"
                    xysize (236, 2)
                    pos (0, 18)
                    background "#FFFFFF80"

                if not minimised_history:
                    if editor.changes:
                        $ n = 0
                        $ nn = 0
                        for k, v in editor.changes.iteritems():
                            $ n += 1
                            $ nn += len(v)
                        text "[nn] changes in [n] files" size 10 color "#FFF" xalign 0.5 ypos 26 outlines [(1, "#00000080", 1, 0)]

                        frame:
                            style "empty"
                            xsize 236
                            ymaximum 400
                            yfill True
                            ypos 42

                            side "c r":
                                area (0, 0, 236, 400)

                                viewport id "editor_history":
                                    draggable False
                                    mousewheel True

                                    vbox:
                                        for fn in editor.changes.iterkeys():
                                            text (fn.split("/")[-1]) size 10 color "#FFF" xalign 0.5 outlines [(1, "#00000080", 1, 0)]
                                            frame style "empty" xysize (236, 2) background "#FFFFFF80"

                                            for l in editor.changes[fn].iterkeys():
                                                textbutton "Line [l]":
                                                    text_size 10
                                                    text_color "#FFF"
                                                    text_outlines [(1, "#00000080", 1, 0)]
                                                    if editor.line == l:
                                                        background "#FFFFFF80"
                                                    tooltip editor.get_tooltip(fn, l)
                                                    action Function(editor.launch_editor, file=fn, line=l)
                                vbar value YScrollValue("editor_history") xsize 10
                    else:
                        text "No history." size 15 color "#FFF" align (0.5, 0.5) outlines [(1, "#00000080", 1, 0)]
