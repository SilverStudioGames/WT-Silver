init python:
    def FileJsonSave(d):
        d["day"] = game.day
        d["playtime"] = renpy.get_game_runtime()
        d["version"] = version_float()

    config.save_json_callbacks.append(FileJsonSave)

    def FileCompatible(slot, page=None):
        version = FileJson(slot, "version", missing=1.0, page=page)

        if version is not None:
            return version >= compatible_version
        return False
