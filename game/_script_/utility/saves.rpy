init python:
    def FileJsonSave(d):
        d["day"] = game.day
        d["playtime"] = renpy.get_game_runtime()

    config.save_json_callbacks.append(FileJsonSave)

    def FileCompatible(slot, page=None):
        ver = FileJson(slot, "_version", missing=0, page=page)
        if ver is not None:
            try:
                return float(ver) >= compatible_version
            except:
                return False
        return True
