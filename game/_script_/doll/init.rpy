# To add new doll character just add it to this named set inside your mod file
init offset = 2
define CHARACTERS = {"hermione", "tonks", "astoria", "cho", "luna", "susan"}

init python:
    def wardrobe_init():
        for c in CHARACTERS:
            char = get_character_object(c)
            outfit = get_character_outfit(c)

            char.equip(outfit)
