# base potions:
# Polyjuice potion (Luna, Cat, Lamia)
# Expanding Elixir (Breast, Ass)
# Moreish mead (cum)
# Transparent tincture (Transparency potion)
# Coloring concoction (hair colors)

# Cum addiction = Moreish mead? + wormwood + your cum
# Ass expansion = Expanding Elixir + knotgrass
# Breast expansion = Expanding Elixir + Root of aconite
# Cat potion = Polyjuice + Cat hair
# Luna potion = Polyjuice + Luna's hair
# Lamia potion = Polyjuice + Basilisk scale
# Transparency potion = Transparent tincture + Niffler's fancy

# Cum addiction: wormwood+your cum (jerk off into it)
# Ass expansion: knotgrass
# Breast expansion: Root of aconite
# Luna potion: Luna's hair
# Transparency potion:  Niffler's fancy
# Lamia potion: Basilisk scale


# wormwood = forbidden forest
# knotgrass = ?
# root_of_aconite =?
# cat_hair
# luna_hair = brush from room?
# basilisk_scale = ?


# all the metadata for the objects is stored statically any information
# that needs to be persistent is stored in a separate known dict value
default potion_lib = PotionCollection(
    lib = [
        PotionIngredient(
            id = "ing_wormwood",
            name = "Wormwood",
            effect = "",
            description = "Wormwood is sometimes found in the forbidden forest.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_knotgrass",
            name = "Knotgrass",
            effect = "",
            description = "You can sometimes find Knotgrass by the forbidden forest.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_aconite_root",
            name = "Root of Aconite",
            effect = "",
            description = "Root of Aconite can be found down by the lake.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_niffler_fancy",
            name = "Niffler's fancy",
            effect = "",
            description = "*Hmm*... I think I heard that it's found by the lake.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_luna_hair",
            name = "Luna's Hair",
            effect = "",
            description = "The hair of Luna Lovegood.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_cat_hair",
            name = "Cat Hair",
            effect = "",
            description = "The hair of a common cat.",
            picture = ""
        ),
        PotionIngredient(
            id = "ing_basilisk_scale",
            name = "Basilisk Scale",
            effect = "",
            description = "The scale of what appears to be a large snake.",
            picture = ""
        ),
        Potion(
            id = "p_transparent_tincture",
            cost = 20,
            whoring_rec = 3,
            name = "Transparent Tincture",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_polyjuice_potion",
            cost = 40,
            whoring_rec = 5,
            name = "Polyjuice Potion",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_expanding_elixir",
            cost = 30,
            whoring_rec = 8,
            name = "Expanding Elixir",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_imperius_potion",
            cost = 45,
            whoring_rec = 14,
            name = "Imperius Potion",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_moreish_mead",
            cost = 60,
            whoring_rec = 14,
            name = "Moreish Mead",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_cum_addiction",
            ingredients = ["ing_wormwood","p_moreish_mead"],
            name = "Cum Addiction Potion",
            effect = "Cum Addiction",
            start_label = "potion_scene_3_1_1",
            description = ""
        ),
        Potion(
            id = "p_ass_expansion",
            ingredients = ["ing_knotgrass","p_expanding_elixir"],
            name = "Ass Expansion Potion",
            effect = "Ass Expansion",
            start_label = "potion_scene_2_2",
            description = ""
        ),
        Potion(
            id = "p_breast_expansion",
            ingredients = ["ing_aconite_root","p_expanding_elixir"],
            name = "Breast Expansion Potion",
            effect = "Breast Expansion",
            start_label = "potion_scene_2_1_1",
            description = ""
        ),
        Potion(
            id = "p_cat_transformation",
            ingredients = ["ing_cat_hair","p_polyjuice_potion"],
            name = "Cat Transformation Potion",
            effect = "Cat Ears",
            start_label = "potion_scene_1_1_1",
            description = ""
        ),
        Potion(
            id = "p_luna_transformation",
            ingredients = ["ing_luna_hair","p_polyjuice_potion"],
            name = "Luna Transformation Potion",
            effect = "Luna Potion",
            start_label = "potion_scene_1_2",
            description = ""
        ),
        Potion(
            id = "p_lamia_transformation",
            ingredients = ["ing_basilisk_scale","p_polyjuice_potion"],
            name = "Lamia Transformation Potion",
            start_label = "potion_scene_1_3",
            effect = "Snek",
            description = ""
        ),
        Potion(
            id = "p_transparency",
            ingredients = ["ing_niffler_fancy","p_transparent_tincture"],
            name = "Transparency Potion",
            effect = "Transparent Clothes",
            start_label = "potion_scene_4",
            description = ""
        ),
        Potion(
            id = "p_hypno",
            ingredients = ["ing_aconite_root","p_imperius_potion"],
            name = "Hypno Potion",
            effect = "Hypno Potion",
            start_label = "potion_scene_3_3_1",
            description = ""
        ),
        Potion(
            id = "p_clone",
            ingredients = ["p_polyjuice_potion","p_imperius_potion"],
            name = "Clone Potion",
            effect = "Clone Potion",
            start_label = "potion_scene_1_4",
            description = ""
        ),
        Potion(
            id = "p_milk_potion",
            name = "Lactantium",
            effect = "Lactantium",
            start_label = "potion_scene_11",
            description = ""
        ),
        Potion(
            id = "p_veritaserum",
            name = "Veritaserum",
            effect = "",
            description = ""
        ),
        Potion(
            id = "p_voluptatem",
            name = "Voluptatem",
            effect = "Voluptatem",
            start_label = "potion_scene_3_4_1",
            description = ""
        )
    ]
)

default potion_inv = PotionInventory()
default p_inv = {} # this stores the id and quantity of items the player has persistently

### Potions Room ###

screen potions_room():
    tag room_screen

    if game.daytime:
        add "images/rooms/_bg_/corridor.webp" #Need day image.
    else:
        add "images/rooms/_bg_/corridor.webp"

    zorder 0

label potions_room:
    show screen blkfade
    with d3

    call room("potions_room")
    call gen_chibi("hide")

    if store_intro_done:
        call gen_chibi("stand", "left", "base")
        call hide_blkfade
    else:
        call gen_chibi("stand", 0, "base")
        call hide_blkfade
        call gen_walk("left", "base")
    pause.2
    jump potions_menu

label potions_menu:
    python:
        items_menu = []
        for potion in potion_lib.get_craftables():
            if potion_inv.can_craft(potion):
                items_menu.append(potion.get_craft_menu_item())
            else:
                items_menu.append(potion.get_craft_menu_item(True))

        items_menu.append(("-Never mind-", "nvm"))
        potion_choice = renpy.display_menu(items_menu)

    if potion_choice == "nvm":
        jump return_office
    elif isinstance(potion_choice, Potion):
        $ renpy.say( None, potion_choice.get_mix_text() )
        if potion_choice.id == "p_cum_addiction":
            ">... but it's missing the most important part."
            menu:
                "-Cum into the Potion-":
                    # TODO: add jerk_off here at some point
                    ">you cum into the potion"
        $ renpy.say(None,">You received the item: \""+potion_choice.name+"\".")
        python:
            for ingredient in potion_choice.ingredients:
                potion_inv.remove(ingredient)
        $ potion_inv.add(potion_choice.id)
    else:
        show screen blktone
        ">You lack the required materials to make this."
        $ missing_items = []
        $ tmp_txt = "You still need "
        python:
            for item in potion_choice:
                if not potion_inv.has(item):
                    missing_items.append(item)
            for i in xrange(len(missing_items)):
                tmp_txt += "{size=+5}{b}"+potion_lib.get_name_by_id(missing_items[i])+"{/b}{/size}"
                if len(missing_items) > 1:
                    if i < len(missing_items)-2:
                        tmp_txt += ", "
                    if i == len(missing_items)-2:
                        tmp_txt += " and "
        $ tmp_txt += " to craft this"
        $ renpy.say(None, tmp_txt)
        #$ renpy.say(None,"You need {size=+5}{b}"+potion_lib.get_name_by_id(potion_choice[0])+"{/b}{/size} and {size=+5}{b}"+potion_lib.get_name_by_id(potion_choice[1])+"{/b}{/size} to craft this")
        hide screen blktone
    jump potions_menu


init -1 python:

    class PotionBase(object):
        id = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def __repr__(self):
            return self.id

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.id == other.id
            else:
                return False
        def __ne__(self, other):
            return not self.__eq__(other)

    class Potion(PotionBase):
        id = ""
        cost = 0
        ingredients = []
        name = ""
        effect = ""
        description = ""
        picture = ""
        whoring_rec = 0
        start_label = None

        def get_store_menu_item(self, disabled=False):
            if disabled:
                return gui.menu_item('-{}-'.format(self.name), None, style="disabled")
            else:
                return gui.menu_item('-{}-'.format(self.name), self)

        def get_craft_menu_item(self, disabled=False):
            if disabled:
                return gui.menu_item('-Craft: "{}"-'.format(self.name), self.ingredients, style="disabled")
            else:
                return gui.menu_item('-Craft: "{}"-'.format(self.name), self.id)

        def get_mix_text(self):
            return ">You mix the {i}" + potion_lib.get_name_by_id(self.ingredients[0]) \
                + "{/i} with the {i}" + potion_lib.get_name_by_id(self.ingredients[1]) + "{/i}"


    class PotionIngredient(PotionBase):
        id = ""
        cost = 0
        name = ""
        effect = ""
        description = ""
        picture = ""


    class PotionCollection(object):
        lib = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_name_by_id(self,id):
            for item in self.lib:
                if item.id == id:
                    return item.name
            return None

        def is_valid_id(self, id):
            for item in self.lib:
                if item.id == id:
                    return True
            return False

        def get_id_by_name(self, name):
            for item in self.lib:
                if item.name == name:
                    return item.id
            return None

        def get_craftables(self):
            craftable = []
            for item in self.lib:
                if hasattr(item, 'ingredients') and len(item.ingredients) > 0:
                    craftable.append(item)
            return craftable

        def get_buyables(self):
            buyable = []
            for item in self.lib:
                if hasattr(item, 'cost') and item.cost > 0:
                    buyable.append(item)
            return buyable

        def get_start_label(self, id):
            for item in self.lib:
                if hasattr(item, 'start_label') and item.id == id:
                    return item.start_label
            return None

        def get_playables(self):
            requests = []
            for item in self.lib:
                if hasattr(item, 'start_label') and item.start_label != None:
                    requests.append(item)
            return requests



    class PotionInventory(object):

        def can_craft(self, potion):
            global p_inv
            for ing_id in potion.ingredients:
                if ing_id in p_inv.keys():
                    if p_inv[ing_id] < 1:
                        return False
                else:
                    return False
            return True

        def has(self, potion):
            global p_inv
            if isinstance(potion, Potion):
                potion = potion.id
            return potion in p_inv.keys()

        def add(self, potion, quant=1):
            global p_inv, potion_lib
            if isinstance(potion, Potion):
                potion = potion.id
            if potion_lib.get_id_by_name(potion) != None:
                potion = potion_lib.get_id_by_name(potion)
            if potion_lib.is_valid_id(potion):
                if potion in p_inv.keys():
                    p_inv[potion] = p_inv[potion] + quant
                else:
                    p_inv[potion] = quant
                return True
            else:
                return False

        def extend(self, list):
            for item in list:
                self.add(item)

        def remove(self, potion, quant=1):
            global p_inv
            if isinstance(potion, Potion):
                potion = potion.id
            if potion in p_inv.keys():
                p_inv[potion] = p_inv[potion] - quant
                if p_inv[potion] < 1:
                    p_inv.pop(potion, None)
                return True
            else:
                return False
