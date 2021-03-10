
default puzzle_box_ITEM = Item("puzzle_box", "quest", "Puzzle Box", 0, "A wooden box with a slide puzzle located on top of it. It was found hidden behind one of the loose bricks in the fireplace. Who knows what's inside.", limit=1, label="puzzle_minigame", unlocked=False)
default collar_ITEM = Item("collar", "quest", "Metal Collar", 0, "A metal collar that can be snapped around ones neck. It radiates magic.", limit=1, label="collar_scene", unlocked=False)
default lootbox_ITEM = Item("cards", "quest", "Pack of Cards", 0, "A pack of wizard cards. You won't know what's inside until you open it.", label="card_lootbox", unlocked=False)
default sealed_scroll_ITEM = Item("sealed_scroll", "quest", "Sealed Scroll", 500, "The scroll can be used to transmute one-self into.. something.\n{size=-4}Hint: The user can't be a virgin.{/size}", limit=1, label="tentacle_scene_intro")
default quidditchguide_ITEM = Item("quidditch_book", "quest", "Quidditch Guide", 200, "This book contains the basic knowledge of Quidditch.", label="quidditch_guide_book", limit=1, image="interface/icons/generic_book.webp", unlocked=False)

# Outfits related quest items
default poker_outfit_ITEM = Item("her_outfit_poker", "quest", "Poke-her-nips Outfit", 15, "An outfit that doesn't leave much for the mind's desire, perfect for a lewd card loving girl.", limit=1, image="interface/icons/icon_gambler_hat.webp", unlocked=False, currency="tokens")
default ball_outfit_ITEM = Item("her_outfit_ball", "quest", "Classy Ball Dress", 0, "A fancy dress for a fancy witch.", limit=1, image="interface/icons/icon_gambler_hat.webp", unlocked=False)
default maid_outfit_ITEM = Item("her_outfit_maid", "quest", "French Maid Costume", 0, "A classic Maid Outfit for a classy Witch.", limit=1, image="interface/icons/feather_duster.webp", unlocked=False)
