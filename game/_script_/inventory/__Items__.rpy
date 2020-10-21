

# Quest Items
default puzzle_box_quest_ITEM = Item(id="puzzle_box", name="Puzzle Box", type="quest item", image="icon_puzzle", description="A wooden box with a slide puzzle located on top of it. It was found hidden behind one of the loose bricks in the fireplace. Who knows what's inside.", event="start_slide_puzzle")
default collar_quest_ITEM = Item(id="collar_quest", name="Collar", type="quest item", image="icon_collar", description="Quest Item!")
default lootbox_quest_ITEM = Item(id="lootbox", name="Pack of cards", type="quest item", image="cards", description="A pack of cards.", cost=100, event="card_lootbox")
default sealed_scroll_quest_ITEM = Scroll(id="sealed_scroll", name="Forbidden Scroll", cost=500, type="scroll", image="item_scroll_sealed", description="The scroll can be used to transmute one-self into.. something.", event="tentacle_scene_intro")

default forbidden_scroll_list = [sealed_scroll_quest_ITEM] # TODO: Replace with quest item list instead.

# Gift items
default lollipop_ITEM          = Item(id="lollipop", name="Lollipop Candy",              cost=20, type="gift", image="item_lollipop", description="A lollipop candy. An adult candy for kids or kids candy for adults?")
default chocolate_ITEM         = Item(id="chocolate", name="Chocolate",                  cost=40, type="gift", image="item_chocolate", description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
default plush_owl_ITEM         = Item(id="plush_owl", name="Plush owl",                  cost=35, type="gift", image="item_plush_owl", description="A Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
default butterbeer_ITEM        = Item(id="butterbeer", name="Butterbeer",                cost=50, type="gift", image="item_butterbeer", description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys.")
default science_mag_ITEM       = Item(id="science_mag", name="Educational Magazines",    cost=30, type="gift", image="item_mag_science", description="Educational magazines. \nthe Trusty companions of every social outcast.")
default girls_mag_ITEM         = Item(id="girls_mag", name="Girly Magazines",            cost=45, type="gift", image="item_mag_girls", description="Girly magazines. \nAll cool girls are reading these.")
default adult_mag_ITEM         = Item(id="adult_mag", name="Adult magazines",            cost=60, type="gift", image="item_mag_adult", description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
default porn_mag_ITEM          = Item(id="porn_mag", name="Porn magazines",              cost=80, type="gift", image="item_mag_porn", description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
default krum_poster_ITEM       = Item(id="krum_poster", name="Viktor Krum Poster",       cost=25, type="gift", image="item_krum_poster", description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
default sexy_lingerie_ITEM     = Item(id="sexy_lingerie", name="Sexy Lingerie",          cost=75, type="gift", image="item_sexy_lingerie", description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
default sexy_stockings_ITEM    = Item(id="sexy_stockings", name="Sexy Stockings",        cost=50, type="gift", image="item_sexy_stockings", description="Somewhere between now and the dark-ages came the invention of stockings, when you want to show some skin but not too much.")
default pink_condoms_ITEM      = Item(id="pink_condoms", name="A Pack Of Condoms",       cost=50, type="gift", image="item_condoms_pink", description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
default vibrator_ITEM          = Item(id="vibrator", name="Vibrator",                    cost=55, type="gift", image="item_vibrator", description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
default anal_lube_ITEM         = Item(id="anal_lube", name="Jar of anal lubricant",      cost=60, type="gift", image="item_anal_lube", description="A Jar of anal lube, Buy this for your loved one - show that you care.")
default ballgag_and_cuffs_ITEM = Item(id="ballgag_and_cuffs", name="Ball gag and cuffs", cost=70, type="gift", image="item_ballgag_and_cuffs", description="Ball gag and cuffs, Turn your soulmate into your cellmate.")
default anal_plugs_ITEM        = Item(id="anal_plugs", name="Anal plugs",                cost=85, type="gift", image="item_anal_plugs", description="Anal plugs decorated with actual tails. Sizes vary to satisfy expert practitioners and beginner alike.")
default testral_strapon_ITEM   = Item(id="testral_strapon", name="Thestral Strap-on",    cost=200,type="gift", image="item_strap_on_testral", description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")
default broom_2000_ITEM        = Item(id="broom_2000", name="Lady Speed Stick-2000",     cost=500,type="gift", image="item_broom", description="{size=-2}The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!{/size}")
default sexdoll_ITEM           = Item(id="sexdoll", name="Sex doll \"Joanne\"",          cost=350,type="gift", image="item_sexdoll", description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
default anal_beads_ITEM        = Item(id="anal_beads", name="Anal beads",                cost=65, type="gift", image="item_anal_beads", description="Anal beads engraved with a strange inscription \"Property of L.C.\".")

default wine_ITEM       = Item(id="wine", name="Wine",             cost=60, type="gift", image="item_wine", description="For the more refined palate.")
default firewhisky_ITEM = Item(id="firewhisky", name="Firewhisky", cost=80, type="gift", image="item_whisky", description="Great taste with a fiery burn.", unlockable=True)

default candy_gift_list = [
    lollipop_ITEM,
    chocolate_ITEM,
]
default drink_gift_list = [
    butterbeer_ITEM,
    wine_ITEM,
    firewhisky_ITEM
]
default mag_gift_list = [
    krum_poster_ITEM,
    science_mag_ITEM,
    girls_mag_ITEM,
    adult_mag_ITEM,
    porn_mag_ITEM,
]
default toy_gift_list = [
    plush_owl_ITEM,
    pink_condoms_ITEM,
    sexy_lingerie_ITEM,
    sexy_stockings_ITEM,
    vibrator_ITEM,
    anal_lube_ITEM,
    ballgag_and_cuffs_ITEM,
    anal_plugs_ITEM,
    testral_strapon_ITEM,
    broom_2000_ITEM,
    sexdoll_ITEM,
    anal_beads_ITEM,
]

default cupboard_drop_list = candy_gift_list + drink_gift_list + mag_gift_list + toy_gift_list

# Posters
default poster_agrabah_ITEM = Item(id="agrabah", name="Agrabah Poster", cost=2, type="poster", image="posters/agrabah", description="A remnant of a distant land and memories about different times. A reminder for when you just want to ponder about what could've been.")
default poster_gryffindor_ITEM = Item(id="gryffindor", name="Gryffindor Poster", cost=2, type="poster", image="posters/gryffindor", description="Make your stance that you support the house of Gryffindor with this themed poster.")
default poster_hufflepuff_ITEM = Item(id="hufflepuff", name="Hufflepuff Poster", cost=2, type="poster", image="posters/hufflepuff", description="Make your stance that you support the house of Hufflepuff with this themed poster.")
default poster_ravenclaw_ITEM = Item(id="ravenclaw", name="Ravenclaw Poster", cost=2, type="poster", image="posters/ravenclaw", description="Make your stance that you support the house of Ravenclaw with this themed poster.")
default poster_slytherin_ITEM = Item(id="slytherin", name="Slytherin Poster", cost=2, type="poster", image="posters/slytherin", description="Make your stance that you support the house of Slytherin with this themed poster.")
default poster_hermione_ITEM = Item(id="hermione", name="Hermione Chibi Poster", cost=2, type="poster", image="posters/hermione", description="A little lewdness for the office, don't worry. With a special illusion charm no one but you will notice a thing...")
default poster_harlots_ITEM = Item(id="harlots", name="Hogwarts Harlots Poster", cost=2, type="poster", image="posters/harlots", description="Hermione showing off her true colours at last with this special poster... illusion charm included...")
default poster_stripper_ITEM = Item(id="stripper", name="Stripper Poster", cost=2, type="poster", image="posters/stripper", description="Hermione showing off how to work the pole... illusion charm included...")
default poster_wanted_ITEM = Item(id="wanted", name="Wanted Poster", cost=2, type="poster", image="posters/wanted", description="A Wild West styled Wanted poster depicting our dear headmaster...")
default poster_tonks_ITEM = Item(id="tonks", name="Tonks Chibi Poster", hidden=True, cost=2, type="poster", image="posters/tonks", description="Somebody anonymous sent us this poster of what we can only suspect is Professor Tonks in the nude!")

# Trophies
default trophy_stag_ITEM = Item(id="stag", name="Stag Head Trophy", cost=3, type="trophy", image="trophies/stag", description="A perfect decoration over your mantelpiece to add a sense of masculinity to the office.")
default trophy_crest_ITEM = Item(id="crest", name="Hogwarts Crest", cost=5, type="trophy", image="trophies/crest", description="A perfect decoration for a headmaster.")

# Pinups & Misc
default pinup_girl_ITEM = Item(id="_deco_1", name="Girl Pinup", cost=0, type="pinup", image="pinups/girl", description="Spice up your cupboard with this sexy pinup model...\n(Shows up when rummaging through the cupboard).", unlocked=True)

# Hats
default owl_hat_ITEM = Item(id="owl_hat", name="Owl Hat", cost=1, type="owl", imagepath="interface/icons/misc/owl_hat.webp", description="A hat for an owl. Don't ask, just accept it..")
default phoenix_hat_ITEM = Item(id="phoenix_hat", name="Phoenix Hat", cost=1, type="phoenix", imagepath="interface/icons/misc/phoenix_hat.webp", description="A little something to make your friend look less depressed.")
default fireplace_hat_ITEM = Item(id="fireplace_hat", name="Skull Hat", cost=1, type="fireplace", imagepath="interface/icons/misc/fireplace_hat.webp", description="Don't let Johnny get a cold!")

default owl_black_ITEM = Item(id="owl_idle_black", name="Black Owl", cost=3, type="mail", imagepath="interface/icons/misc/owl_black.webp", description="Magically dye your mail courier black!")

# Xmas
default fireplace_xmas_ITEM = Item(id="fireplace_tree", name="Christmas Decorations", cost=1, type="fireplace", imagepath="interface/icons/misc/fireplace_xmas.webp", description="Don't let Johnny get a cold!")
default phoenix_xmas_ITEM = Item(id="phoenix_xmas", name="Phoenix Christmas Decorations", cost=1, type="phoenix", imagepath="interface/icons/misc/phoenix_xmas.webp", description="A little something to make your friend look less depressed.")
default owl_xmas_ITEM = Item(id="owl_xmas", name="Owl Christmas hat", cost=1, type="owl", imagepath="interface/icons/misc/owl_xmas.webp", description="A hat for an owl. Don't ask, just accept it..")

default cupboard_halloween_ITEM = Item(id="cupboard_halloween", name="Halloween decorations", cost=0, type="cupboard", imagepath="interface/icons/misc/halloween.webp", description="", unlocked=True)
default fireplace_halloween_ITEM = Item(id="fireplace_halloween", name="Halloween decorations", cost=0, type="fireplace", imagepath="interface/icons/misc/fireplace_halloween.webp", description="", unlocked=True)
default phoenix_halloween_ITEM = Item(id="phoenix_halloween", name="Halloween decorations", cost=0, type="phoenix", imagepath="interface/icons/misc/phoenix_halloween.webp", description="", unlocked=True)

default wall_deco_list = [
    poster_agrabah_ITEM,
    poster_gryffindor_ITEM,
    poster_hufflepuff_ITEM,
    poster_ravenclaw_ITEM,
    poster_slytherin_ITEM,
    poster_hermione_ITEM,
    poster_harlots_ITEM,
    poster_stripper_ITEM,
    poster_wanted_ITEM,
    poster_tonks_ITEM,
]
default fireplace_deco_list = [
    trophy_crest_ITEM,
    trophy_stag_ITEM,
]
default cupboard_deco_list = [
    pinup_girl_ITEM
]
default misc_deco_list = [
    owl_black_ITEM,
    phoenix_xmas_ITEM,
    fireplace_xmas_ITEM,
    cupboard_halloween_ITEM,
    fireplace_halloween_ITEM,
    phoenix_halloween_ITEM,
]
default misc_hat_list = [
    fireplace_hat_ITEM,
    phoenix_hat_ITEM,
    owl_hat_ITEM,
    owl_xmas_ITEM
]

# Scroll Items
default scroll_1_ITEM = Scroll(id="scroll_1",   name="The room",           cost=1,   type="scroll", image="item_scroll", scroll_image="1", comments=["This is a first ever draft of the Dumbledore's office.","Not a very exciting thing to look at, sure. But holds great historical value."])
default scroll_2_ITEM = Scroll(id="scroll_2",   name="The calendar",       cost=2,   type="scroll", image="item_scroll", scroll_image="2", comments=["The calendar...","On the early stages of development I toyed with an idea of implementing an actual in-game calendar into the gameplay...","I soon realised how much more difficult it would be to create a game like that...","And since I personally believe that any time limits in any game always work against the fun factor I decided to abandon the idea...","Later on I used this drawing as a parchment paper for letters to be written on..."])
default scroll_3_ITEM = Scroll(id="scroll_3",   name="The girl",           cost=10,  type="scroll", image="item_scroll", scroll_image="3", comments=["A couple of very early drawings of Hermione..."])
default scroll_4_ITEM = Scroll(id="scroll_4",   name="Deepthroating",      cost=60,  type="scroll", image="item_scroll", scroll_image="4", comments=["The deepthroating scene...","My first attempt.","Been deemed unworthy and ended up here."])
default scroll_5_ITEM = Scroll(id="scroll_5",   name="Poster 01",          cost=50,  type="scroll", image="item_scroll", scroll_image="5", comments=["The game poster...","Hermione is Dahr's work. The rest is me..."])
default scroll_6_ITEM = Scroll(id="scroll_6",   name="Poster 02",          cost=50,  type="scroll", image="item_scroll", scroll_image="6", comments=["Alternative game poster.","This one has never been released."])
default scroll_7_ITEM = Scroll(id="scroll_7",   name="Chibi-dancing",      cost=20,  type="scroll", image="item_scroll", scroll_image="7", comments=["Some chibi close-ups.","The one on the left never made it into the final game..."])
default scroll_8_ITEM = Scroll(id="scroll_8",   name="Game items",         cost=10,  type="scroll", image="item_scroll", scroll_image="8", comments=["A bunch of items that I ended up not using...","I blame dahr and his awesome artwork."])
default scroll_9_ITEM = Scroll(id="scroll_9",   name="Panties no panties", cost=50,  type="scroll", image="item_scroll", scroll_image="9", comments=["The drawing of Hermione from the poster. (by Dahr)","I like one on the right with her panties still on."])
default scroll_10_ITEM = Scroll(id="scroll_10", name="A lot of pegs",      cost=50,  type="scroll", image="item_scroll", scroll_image="10", comments=["Another thing that never made it into the final game...","The idea here was that the more you level up Hermione the more pegs she would let you to put on her...","And the nipple chain was supposed to be worn to class under the uniform."])
default scroll_11_ITEM = Scroll(id="scroll_11", name="House-elf brothel",  cost=80,  type="scroll", image="item_scroll", scroll_image="11", comments=["The house-elf brothel... Just another thing that never happened."])
default scroll_12_ITEM = Scroll(id="scroll_12", name="Me and Lola",        cost=10,  type="scroll", image="item_scroll", scroll_image="12", comments=["A drawing featuring yours truly as a Durmstrung mage and Lola as a student...","The drawing itself is by Dahr of course."])
default scroll_13_ITEM = Scroll(id="scroll_13", name="Hard training",      cost=80,  type="scroll", image="item_scroll", scroll_image="13", comments=["Another one of those side-quests that never happened...","This one was about--","No, I better not. Who knows, maybe we will get to adding those quests eventually."])
default scroll_14_ITEM = Scroll(id="scroll_14", name="Wizard's Chess",     cost=50,  type="scroll", image="item_scroll", scroll_image="14", comments=["Another sub-quest...","This one involving the school's wizard chess club."])
default scroll_15_ITEM = Scroll(id="scroll_15", name="Tutoring books",     cost=10,  type="scroll", image="item_scroll", scroll_image="15", comments=["There is more then one way for a pretty girl to carry her books around.","I thought it would be cool to change the way Hermione carries the books as she progresses with her training.","Since the whole tutoring arc got canceled I am showing it here..."])

default scroll_16_ITEM = Scroll(id="scroll_16", name="Extra gifts 01",     cost=10,  type="scroll", image="item_scroll", scroll_image="16", comments=["A couple of items that didn't make it into the final game...","The one on the left is an actual live house-elf to give as a present.","The one on the right is a portrait of a pervy but wise wizard. Supposed to be helping with studying..."])
default scroll_17_ITEM = Scroll(id="scroll_17", name="Extra gifts 02",     cost=10,  type="scroll", image="item_scroll", scroll_image="17", comments=["Few more items...","A newspaper, a bottle of perfume and a magical hat that says things you want to hear..."])
default scroll_18_ITEM = Scroll(id="scroll_18", name="Fiction books",      cost=10,  type="scroll", image="item_scroll", scroll_image="18", comments=["The fiction books...","The top row are my sketches, the bottom row are finalised drawings by dahr."])
default scroll_19_ITEM = Scroll(id="scroll_19", name="Singer whore",       cost=60,  type="scroll", image="item_scroll", scroll_image="19", comments=["A drawing of a famous singer.","Has no connection to this game and is here for no reason whatsoever."])
default scroll_20_ITEM = Scroll(id="scroll_20", name="Casting",            cost=60,  type="scroll", image="item_scroll", scroll_image="20", comments=["It took me a while to come up with a proper look for Hermione...","Version \"A\" was my first attempt. And I liked it up until the moment when I started to hate it...","Version \"B\" was my second attempt. And it's good. But her confident and semi-aggressive facial features didn't fit the character well...","Version \"C\" is the one that got the role. The Hermione that we all grew to care for by now, I'm sure."])
default scroll_21_ITEM = Scroll(id="scroll_21", name="Witch robe 01",      cost=20,  type="scroll", image="item_scroll", scroll_image="21", comments=["Sub-quests that never happened.","You are allowed to feel bad for rushing me.","If you did not rush me you are allowed to feel angry at people who did."])
default scroll_22_ITEM = Scroll(id="scroll_22", name="Witch robe 02",      cost=20,  type="scroll", image="item_scroll", scroll_image="22", comments=["Hermione presenting her body to Genie...","This would have been a quite memorable scene..."])
default scroll_23_ITEM = Scroll(id="scroll_23", name="Witch robe 03",      cost=20,  type="scroll", image="item_scroll", scroll_image="23", comments=["Didn't expect this one, did you?","In case you're wondering this is still Hermione."])
default scroll_24_ITEM = Scroll(id="scroll_24", name="Witch robe 04",      cost=20,  type="scroll", image="item_scroll", scroll_image="24", comments=[".................................","Sub-quests of course..."])
default scroll_25_ITEM = Scroll(id="scroll_25", name="The walk",           cost=80,  type="scroll", image="item_scroll", scroll_image="25", comments=["Another sub-quest...","We had a rather lengthy discussion with Dahr about this one...","I was sort of against it, but then Dahr sent me this picture and it made me shut up."])
default scroll_26_ITEM = Scroll(id="scroll_26", name="Durmstrang",         cost=80,  type="scroll", image="item_scroll", scroll_image="26", comments=["One the very early stages of development I had an idea of representing outcomes of your failed or successfully completed sub quests with a simplistic plates, or photographs...","At first many of the sub-quests involved deciding on how to spend the Hogwarts budget...","Spend your money to finance the school quidditch team, or to hire new teachers and such..."])
default scroll_27_ITEM = Scroll(id="scroll_27", name="Gag ball",           cost=80,  type="scroll", image="item_scroll", scroll_image="27", comments=["Isn't she adorable?"])
default scroll_28_ITEM = Scroll(id="scroll_28", name="New clothes 01",     cost=50,  type="scroll", image="item_scroll", scroll_image="28", comments=["Another (rather lengthy) sub-quest..."])
default scroll_29_ITEM = Scroll(id="scroll_29", name="New clothes 02",     cost=50,  type="scroll", image="item_scroll", scroll_image="29", comments=[".........."])
default scroll_30_ITEM = Scroll(id="scroll_30", name="The gang",           cost=10,  type="scroll", image="item_scroll", scroll_image="30", comments=["One of the very early sketches related to the quidditch sub-quests..."])

default scroll_31_ITEM = Scroll(id="scroll_31", name="Silver",           cost=10,  type="scroll", image="item_scroll_silver", scroll_image="31", comments=[""])
#default scroll_32_ITEM = Scroll(id="scroll_32", name="New characters!",   cost=50,  type="scroll", image="item_scroll_silver", scroll_image="32", comments=["More and more characters got added along the way..."])
default scroll_33_ITEM = Scroll(id="scroll_33", name="Lion, Witch, & Wardrobe 1",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="33", comments=["The very first wardrobe that got added to silver."])
default scroll_34_ITEM = Scroll(id="scroll_34", name="Lion, Witch, & Wardrobe 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="34", comments=["The second one already had almost all features from the current one, but didn't look that great..."])
default scroll_35_ITEM = Scroll(id="scroll_35", name="Lion, Witch, & Wardrobe 3",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="35", comments=["The wardrobe got a brand new design, with tons of new features!","Every other girl available in silver has one too!"])

default scroll_37_ITEM = Scroll(id="scroll_37", name="Map 2",   cost=10,  type="scroll", image="item_scroll_silver", scroll_image="37", comments=["First try at the new map.","We removed all the text and labels and replaced them with icons."])

default scroll_list_A = [
    scroll_1_ITEM, scroll_2_ITEM,
    scroll_3_ITEM, scroll_4_ITEM,
    scroll_5_ITEM, scroll_6_ITEM,
    scroll_7_ITEM, scroll_8_ITEM,
    scroll_9_ITEM, scroll_10_ITEM,
    scroll_11_ITEM, scroll_12_ITEM,
    scroll_13_ITEM ,scroll_14_ITEM,
    scroll_15_ITEM,
]
default scroll_list_B = [
    scroll_16_ITEM, scroll_17_ITEM,
    scroll_18_ITEM, scroll_19_ITEM,
    scroll_20_ITEM, scroll_21_ITEM,
    scroll_22_ITEM, scroll_23_ITEM,
    scroll_24_ITEM, scroll_25_ITEM,
    scroll_26_ITEM, scroll_27_ITEM,
    scroll_28_ITEM, scroll_29_ITEM,
    scroll_30_ITEM,
]
default scroll_list_C = [
    scroll_31_ITEM,
    scroll_33_ITEM, scroll_34_ITEM,
    scroll_35_ITEM, scroll_37_ITEM,
]
