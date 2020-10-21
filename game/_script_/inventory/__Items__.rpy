

# Quest Items
default puzzle_box_quest_ITEM = Item(id="puzzle_box", name="Puzzle Box", type="quest item", image="icon_puzzle", description="A wooden box with a slide puzzle located on top of it. It was found hidden behind one of the loose bricks in the fireplace. Who knows what's inside.", event="start_slide_puzzle")
default collar_quest_ITEM = Item(id="collar_quest", name="Collar", type="quest item", image="icon_collar", description="Quest Item!")
default lootbox_quest_ITEM = Item(id="lootbox", name="Pack of cards", type="quest item", image="cards", description="A pack of cards.", cost=100, event="card_lootbox")
default sealed_scroll_quest_ITEM = Scroll(id="sealed_scroll", name="Forbidden Scroll", cost=500, type="scroll", image="item_scroll_sealed", description="The scroll can be used to transmute one-self into.. something.", event="tentacle_scene_intro")

default forbidden_scroll_list = [sealed_scroll_quest_ITEM] # TODO: Replace with quest item list instead.

# Gift items
default lollipop_ITEM          = Item(id="lollipop", name="Lollipop Candy",              cost=20, type="candy", image="item_lollipop", description="A lollipop candy. An adult candy for kids or kids candy for adults?")
default chocolate_ITEM         = Item(id="chocolate", name="Chocolate",                  cost=40, type="candy", image="item_chocolate", description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
default plush_owl_ITEM         = Item(id="plush_owl", name="Plush owl",                  cost=35, type="toy", image="item_plush_owl", description="A Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
default butterbeer_ITEM        = Item(id="butterbeer", name="Butterbeer",                cost=50, type="drink", image="item_butterbeer", description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys.")
default science_mag_ITEM       = Item(id="science_mag", name="Educational Magazines",    cost=30, type="mag", image="item_mag_science", description="Educational magazines. \nthe Trusty companions of every social outcast.")
default girls_mag_ITEM         = Item(id="girls_mag", name="Girly Magazines",            cost=45, type="mag", image="item_mag_girls", description="Girly magazines. \nAll cool girls are reading these.")
default adult_mag_ITEM         = Item(id="adult_mag", name="Adult magazines",            cost=60, type="mag", image="item_mag_adult", description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
default porn_mag_ITEM          = Item(id="porn_mag", name="Porn magazines",              cost=80, type="mag", image="item_mag_porn", description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
default krum_poster_ITEM       = Item(id="krum_poster", name="Viktor Krum Poster",       cost=25, type="mag", image="item_krum_poster", description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
default sexy_lingerie_ITEM     = Item(id="sexy_lingerie", name="Sexy Lingerie",          cost=75, type="", image="item_sexy_lingerie", description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
default sexy_stockings_ITEM    = Item(id="sexy_stockings", name="Sexy Stockings",        cost=50, type="", image="item_sexy_stockings", description="Somewhere between now and the dark-ages came the invention of stockings, when you want to show some skin but not too much.")
default pink_condoms_ITEM      = Item(id="pink_condoms", name="A Pack Of Condoms",       cost=50, type="toy", image="item_condoms_pink", description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
default vibrator_ITEM          = Item(id="vibrator", name="Vibrator",                    cost=55, type="toy", image="item_vibrator", description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
default anal_lube_ITEM         = Item(id="anal_lube", name="Jar of anal lubricant",      cost=60, type="toy", image="item_anal_lube", description="A Jar of anal lube, Buy this for your loved one - show that you care.")
default ballgag_and_cuffs_ITEM = Item(id="ballgag_and_cuffs", name="Ball gag and cuffs", cost=70, type="toy", image="item_ballgag_and_cuffs", description="Ball gag and cuffs, Turn your soulmate into your cellmate.")
default anal_plugs_ITEM        = Item(id="anal_plugs", name="Anal plugs",                cost=85, type="toy", image="item_anal_plugs", description="Anal plugs decorated with actual tails. Sizes vary to satisfy expert practitioners and beginner alike.")
default testral_strapon_ITEM   = Item(id="testral_strapon", name="Thestral Strap-on",    cost=200,type="toy", image="item_strap_on_testral", description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")
default broom_2000_ITEM        = Item(id="broom_2000", name="Lady Speed Stick-2000",     cost=500,type="toy", image="item_broom", description="{size=-2}The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!{/size}")
default sexdoll_ITEM           = Item(id="sexdoll", name="Sex doll \"Joanne\"",          cost=350,type="toy", image="item_sexdoll", description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
default anal_beads_ITEM        = Item(id="anal_beads", name="Anal beads",                cost=65, type="toy", image="item_anal_beads", description="Anal beads engraved with a strange inscription \"Property of L.C.\".")

default wine_ITEM       = Item(id="wine", name="Wine",             cost=60, type="drink", image="item_wine", description="For the more refined palate.")
default firewhisky_ITEM = Item(id="firewhisky", name="Firewhisky", cost=80, type="drink", image="item_whisky", description="Great taste with a fiery burn.", unlockable=True)

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

# Hermione

default hg_bikini1 = CostumeItem(
    id="hg_bikini1", name="Rave Bikini", type="outfit", items=["bikini-bra","thong"],
    cost=her_outfit_bikini1.price, wait_time=2, image=her_outfit_bikini1, description="> A Bunch of straps for a bunch of gold!")

default hg_bikini2 = CostumeItem(
    id="hg_bikini2", name="Leather Bikini", type="outfit", items=["bikini-bra","thong"],
    cost=her_outfit_bikini2.price, wait_time=2, image=her_outfit_bikini2, description="> Emits a slight squeaking sound when rubbed.")

default hg_maid = CostumeItem(
    id="hg_maid", name="French Maid Costume", type="outfit", items=["hat","choker","top","gloves","stockings"],
    cost=her_outfit_maid.price, wait_time=3, image=her_outfit_maid, description="> A classic Maids Outfit for a classy Witch.")

default hg_bunny = CostumeItem(
    id="hg_bunny", name="Sexy Bunny Costume", type="outfit", items=["hat","bowtie","onepiece-top","gloves","tattoo","stockings"],
    cost=her_outfit_bunny.price, wait_time=2, image=her_outfit_bunny, description="> A Bunny costume for a bouncy girl.")

default hg_ball = CostumeItem(
    id="hg_ball", name="Classy Ball Dress", type="outfit", items=["earrings","necklace","onepiece-top","sash"],
    cost=her_outfit_ball.price, wait_time=7, image=her_outfit_ball, description="> A fancy dress for a fancy witch.")

default hg_yennefer = CostumeItem(
    id="hg_yennefer", name="Yennefer Costume", type="outfit", items=["pendant","scarf","feathers","top","corset","gloves","bottoms","belt","sash","stockings"],
    cost=her_outfit_yennefer.price, wait_time=3, image=her_outfit_yennefer, description="> An outfit which smells like lilac and gooseberries.")

default hg_bioshock = CostumeItem(
    id="hg_bioshock", name="Bioshock Costume", type="outfit", items=["choker","top","jacket","bottoms"],
    cost=her_outfit_bioshock.price, wait_time=3, image=her_outfit_bioshock, description="> Flick some coins for this shockingly inspirational outfit.")

default hg_swimsuit = CostumeItem(
    id="hg_swimsuit", name="Swimsuit", type="outfit", items=["onepiece-top"],
    cost=her_outfit_swimsuit.price, wait_time=2, image=her_outfit_swimsuit, description="> A swimsuit for witches who love getting wet.")

default hg_egypt = CostumeItem(
    id="hg_egypt", name="Egyptian", type="outfit", items=["neck-band","top","arm bands","onepiece-bottoms"],
    cost=her_outfit_egypt.price, wait_time=2, image=her_outfit_egypt, description="> An Egyptian themed outfit which is probably what Cleopatra once wore.")

default hg_latex_dress = CostumeItem(
    id="hg_latex_dress", name="Latex Dress", type="outfit", items=["onepiece-top"],
    cost=her_outfit_latex_dress.price, wait_time=2, image=her_outfit_latex_dress, description="> Tight fitting and something you wouldn't normally find in a regular clothing store.")

default hg_nightie = CostumeItem(
    id="hg_nightie", name="Nightie", type="outfit", items=["onepiece-top"],
    cost=her_outfit_nightie.price, wait_time=2, image=her_outfit_nightie, description="> Comfortable alternative for a pyjamas.")

default hg_poker = CostumeItem(
    id="hg_poker", name="Poke-her-nips Outfit", type="outfit_token", items=["hat","earrings","bowtie","onepiece-bra","panties","stockings"],
    cost=10, wait_time=3, image=her_outfit_poker, description="> An outfit that doesn't leave much for the mind's desire, perfect for a lewd card loving girl.")

default hg_tifa = CostumeItem(
    id="hg_tifa", name="Tifa Cosplay", type="outfit", items=["top","gloves","suspenders","belt","bottoms"],
    cost=her_outfit_tifa.price, wait_time=3, image=her_outfit_tifa, description="> An outfit for when your sexual fantasies are just getting started.")

default hg_msmarv = CostumeItem(
    id="hg_msmarv", name="Ms. Marvel Cosplay", type="outfit", items=["onepiece-top","gloves","sash","stockings"],
    cost=her_outfit_msmarv.price, wait_time=2, image=her_outfit_msmarv, description="> For the girl that likes the lightning bolt better on the chest than the forehead.")

default hg_hslut = CostumeItem(
    id="hg_hslut", name="Heart Slut", type="outfit", items=["earrings","necklace","top","tassel-bra","gloves","garter-belt","stockings"],
    cost=her_outfit_hslut.price, wait_time=2, image=her_outfit_hslut, description="> A sexy dancers outfit with heart shaped nipple tassels.")

default hg_croft = CostumeItem(
    id="hg_croft", name="Lora Craft Cosplay", type="outfit", items=["top","shoulder-straps","bottoms","belt-holster"],
    cost=her_outfit_croft.price, wait_time=2, image=her_outfit_croft, description="> An outfit perfectly suited for exploring deep, dark and moist caverns.")

default hg_witch = CostumeItem(
    id="hg_witch", name="Halloween Witch Cosplay", type="outfit", items=["onepiece-top","cape","stockings"],
    cost=her_outfit_witch.price, wait_time=2, image=her_outfit_witch, description="> Release your inner witch with this Halloween inspired outfit.")

default hg_latex = CostumeItem(
    id="hg_latex", name="Latex Outfit", type="outfit", items=["choker","top","gloves","panties","stockings"],
    cost=her_outfit_latex.price, wait_time=2, image=her_outfit_latex, description="> A tight fitting outfit that takes about twenty minutes to put on properly.")

default hg_slutty_schoolgirl = CostumeItem(
    id="hg_slutty_schoolgirl", name="Slutty Schoolgirl", type="outfit", items=["top","bottoms","stockings"],
    cost=her_outfit_slutty_schoolgirl.price, wait_time=2, image=her_outfit_slutty_schoolgirl, description="> A arguably better version of the regular school outfit")

default hg_teddy = CostumeItem(
    id="hg_teddy", name="Teddy Nightie", type="outfit", items=["top"],
    cost=her_outfit_teddy.price, wait_time=2, image=her_outfit_teddy, description="> A more airy nightdress leaving not much fabric between you and your bed.")

default hg_fishnet = CostumeItem(
    id="hg_fishnet", name="Fishnet Outfit", type="outfit", items=["top","panties"],
    cost=her_outfit_fishnet.price, wait_time=2, image=her_outfit_fishnet, description="> An outfit for when fishnet stockings isn't enough. {size=-4}Dislaimer: Not effective for catching actual fish.{/size}")

default hg_bikini3 = CostumeItem(
    id="hg_bikini3", name="Sling Bikini Outfit", type="outfit", items=["bra","panties"],
    cost=her_outfit_bikini3.price, wait_time=2, image=her_outfit_bikini3, description="> An outfit providing some coverage.")

default hg_cheerleader = CostumeItem(
    id="hg_cheerleader", name="Gryffindor Cheerleader Outfit", type="outfit", items=["top", "bottoms", "gloves"],
    cost=her_outfit_cheerleader_1.price, wait_time=2, image=her_outfit_cheerleader_1, description="> So daring and bold, sporting red and gold!")

default hg_cheerleader2 = CostumeItem(
    id="hg_cheerleader2", name="Slutty Gryffindor Cheerleader Outfit", type="outfit", items=["top", "bottoms"],
    cost=her_outfit_cheerleader_2.price, wait_time=2, image=her_outfit_cheerleader_2, description="> So daring and bold, sporting red and gold!")

default hermione_outfits_list = [hg_maid, hg_cheerleader, hg_bunny, hg_ball, hg_yennefer, hg_bioshock, hg_swimsuit, hg_egypt, hg_latex_dress, hg_nightie, hg_tifa, hg_msmarv, hg_hslut, hg_croft, hg_witch, hg_latex, hg_slutty_schoolgirl, hg_teddy, hg_fishnet, hg_bikini3, hg_bikini1, hg_bikini2, hg_cheerleader2]

default hermione_costumes_list = [] # TODO: Remove
default hermione_dresses_list = [] # TODO: Remove
default hermione_clothing_sets_list=[] # TODO: Remove

# Luna Outfits

default ll_stewardess_ITEM = CostumeItem(
    id="ll_stewardess", name="Stewardess Outfit", type="outfit", items=["onepiece-top","hat","necklace","thong"],
    cost=80, wait_time=2, image="outfits/ll_stewardess", description="> An outfit giving you immediate access to the mile-high club!",
    # Layers
    outfit_layers = ["panties/panties_thong_1","onepieces/onepiece_stewardess_1","neckwear/cloth_tie"],
    top_layers    = "hat_stewardess"
)
default ll_stewardess_short_ITEM = CostumeItem(
    id="ll_stewardess_short", name="Short Stewardess Outfit", type="outfit", items=["onepiece-top","hat","necklace","thong"], image="outfits/ll_stewardess_short", unlockable=True,
    # Layers
    outfit_layers = ["panties/panties_thong_2","onepieces/onepiece_stewardess_2","neckwear/cloth_tie"],
    top_layers    = "hat_stewardess"
)
default ll_dress_orange_ITEM = CostumeItem(
    id="ll_dress_orange", name="Ball Dress", type="outfit", items=["earrings","onepiece-top","stockings"],
    cost=200, wait_time=3, image="outfits/ll_dress_orange", description=">A cute dress in a questionable colour.",
    # Layers
    outfit_layers = ["stockings/leggings_1","onepieces/onepiece_ball_dress","piercings/ears_starts_1"]
)

default luna_outfits_list = []
default luna_costumes_list = [
    ll_stewardess_ITEM,
    ll_stewardess_short_ITEM,
]
default luna_dresses_list = [
    ll_dress_orange_ITEM,
]

# Luna Sets
default ll_cheer_r_ITEM       = Item(id="ll_cheer_r", name="Ravenclaw Cheerleader", type="set", items=["top","bottoms","stockings"], cost=80, wait_time=2, image="outfits/ll_cheer_r", description=">The Ravenclaw version of the Cheerleader attire.")
default ll_lingerie_silk_ITEM = Item(id="ll_lingerie_silk", name="Silk Lingerie",   type="set", items=["bra","panties"], cost=80, wait_time=1, image="outfits/ll_lingerie_silk", description=">A smooth and comfortable silk bra and panty set.")

default ll_quirky_muggle_ITEM = Item(id="ll_quirky_muggle", name="Quirky Muggle", type="set", items=["top","bottoms","stockings"], image="outfits/ll_muggle_1", unlockable=True)

default luna_clothing_sets_list = [
    ll_cheer_r_ITEM,
    ll_lingerie_silk_ITEM,
    ll_quirky_muggle_ITEM,
]

init offset = 1 # Initialize chunk after character class

default ag_anntakamaki_ITEM = Item(id="ag_ann_takamaki", name="Ann Takamaki Cosplay Outfit", type="outfit", items=["onepiece-top","gloves", "boots", "butt-plug", "mask", "hairstyle"], image=ast_outfit_ann, cost=600, wait_time=2, description="> Legend says that the one who wears it will look like a different persona...")

default astoria_outfits_list=[
    #ag_boss_uniform_ITEM,
]
default astoria_costumes_list = [
    #ag_costume_lazy_town_ITEM,
    #ag_costume_lazy_town_short_ITEM,
]
default astoria_dresses_list=[
    #ag_dress_yule_ball_ITEM,
]

default astoria_clothing_sets_list = [
    ag_anntakamaki_ITEM
]

init offset = 0 # Back to normal

# Susan Outfits
default susan_outfits_list = []
default susan_costumes_list = []
default susan_dresses_list = []

# Susan Sets
default susan_clothing_sets_list = []

# Cho outfits
init offset = 1

default cc_dress_red_ITEM = CostumeItem(
    id="cc_dress_red", name="Traditional Dress in Red", type="outfit", items=["onepiece-top"],
    cost=100, wait_time=3, image=cho_outfit_dress1, description="> A traditional dress inspired by Chinese culture.",
    # Layers
    outfit_layers = ["onepieces/onepiece_ball_dress"]
)

default cc_outfit_sailor_white_ITEM = CostumeItem(
    id="cc_outfit_sailor_white", name="White Sailor Outfit", type="outfit", items=["hat","top","bottoms","thong","stockings"],
    cost=240, wait_time=3, image=cho_outfit_sailor, description="> A slutty sailor outfit, perfect for the average cannon swabber."
)

default cc_costume_misty_ITEM = CostumeItem(
    id="cc_costume_misty", name="Misty Costume", type="outfit", items=["top","bottoms","suspenders"],
    cost=100, wait_time=2, image=cho_outfit_misty, description="> For trainers that want to be the very best! To train them is your cause!",
    # Layers
    outfit_layers = ["tops/top_shirt_1","bottoms/pants_short_1","../body/arms/arm_down_l_overlay","accs/suspenders_1"]
)

default cc_japanese_school_uniform_ITEM = CostumeItem(
    id="cc_japanese_school_uniform", name="Japanese School Uniform", type="outfit", items=["top","bottoms","stockings"],
    cost=300, wait_time=3, image=cho_outfit_j_school, description="> A school girl uniform inspired by the land of culture.",
    # Layers
    outfit_layers = ["tops/top_j_school_1","bottoms/j_school_skirt_1","../body/arms/arm_down_l_overlay","stockings/kneehigh"]
)

# Cho Sets
default cc_muggle_hot_ITEM = Item(id="cc_muggle_hot", name="Hot Weather Clothing", type="set", items=["top","bottoms","stockings"], image=cho_outfit_trainee, unlockable=True)
default cc_party_slut_ITEM = Item(id="cc_party", name="Party Clothing", type="set", items=["bra","bottoms"], image=cho_outfit_party, unlockable=True)

default cc_lingerie_lace_ITEM = Item(id="cc_lingerie_lace", name="Lace Lingerie", type="set", items=["earrings","choker","bra","garter-belt","panties","stockings"], image=cho_outfit_lacelingerie, cost=500, wait_time=2, description="> This lingerie set turns even the toughest tomboy into a cute and sexy princess!")
default cc_bikini_micro_ITEM  = Item(id="cc_bikini_micro", name="Micro Bikini", type="set", items=["bra","panties"], image=cho_outfit_bikini, cost=69, wait_time=2, description="> The regular size bikinis are out of stock...")
default cc_smurfette_ITEM = Item(id="cc_smurfette", name="Smurfette Cosplay Outfit", type="set", items=["top","hat","hairstyle"], image=cho_outfit_smurfette, cost=0, wait_time=1, description="> Unleash your inner blue!")

default cho_outfits_list = [
    cc_outfit_sailor_white_ITEM, cc_japanese_school_uniform_ITEM
]
default cho_costumes_list = [
    cc_costume_misty_ITEM
]
default cho_dresses_list = [
    cc_dress_red_ITEM
]

default cho_clothing_sets_list = [
    cc_muggle_hot_ITEM,
    cc_party_slut_ITEM,
    cc_lingerie_lace_ITEM,
    cc_bikini_micro_ITEM,
]

init offset = 0

init offset = 1 # Initialize chunk after character class

default nt_school = Item(id="nt_school", name="Schoolgirl Outfit", type="outfit", items=["top", "skirt"], image=ton_outfit_school, cost=ton_outfit_school.price, wait_time=2, description="> A very tight school outfit back from 1995!")
default nt_casual = Item(id="nt_casual", name="Casual Outfit", type="outfit", items=["top", "trousers"], image=ton_outfit_casual, cost=ton_outfit_casual.price, wait_time=2, description="> Very retro.")
default nt_nightie = Item(id="nt_nightie", name="Nightie Outfit", type="outfit", items=["top"], image=ton_outfit_nightie, cost=ton_outfit_nightie.price, wait_time=2, description="> Doesn't leave much for the imagination.")
default nt_bunny = Item(id="nt_bunny", name="Bunny suit Outfit", type="outfit", items=["one-piece suit", "pantyhose", "necktie"], image=ton_outfit_bunny, cost=ton_outfit_bunny.price, wait_time=2, description="> Vewy cute. :3")
default nt_silky = Item(id="nt_silky", name="Silky Slut Dress", type="outfit", items=["top", "trousers"], image=ton_outfit_silky, cost=ton_outfit_silky.price, wait_time=2, description="> Disclaimer: Madam Mafkin isn't responsible for damaged nipples.")
default nt_bikini_1 = Item(id="nt_bikini_1", name="Simple Bikini", type="outfit", items=["bra", "panties"], image=ton_outfit_bikini_1, cost=ton_outfit_bikini_1.price, wait_time=2, description="It ain't much, but it at least covers the important bits.")
default nt_bikini_2 = Item(id="nt_bikini_2", name="Striped Bikini", type="outfit", items=["bra", "panties"], image=ton_outfit_bikini_2, cost=ton_outfit_bikini_2.price, wait_time=2, description="It ain't much, but it at least covers the important bits. Did I mention the stripes?")
default nt_bikini_3 = Item(id="nt_bikini_3", name="Simple Bikini", type="outfit", items=["bra", "panties"], image=ton_outfit_bikini_3, cost=ton_outfit_bikini_3.price, wait_time=2, description="Show your national integrity by wearing this -- authorised by the Ministry Of Magic -- bikini set!")
default nt_bikini_4 = Item(id="nt_bikini_4", name="Simple Bikini", type="outfit", items=["bra", "panties"], image=ton_outfit_bikini_4, cost=ton_outfit_bikini_4.price, wait_time=2, description="Label yourself a national traitor by wearing this -- authorised by the Ministry of Magic -- bikini set!")

default tonks_clothing_sets_list = [
    nt_school,
    nt_casual,
    nt_nightie,
    nt_bunny,
    nt_silky,
    nt_bikini_1,
    nt_bikini_2,
    nt_bikini_3,
    nt_bikini_4
]

init offset = 0 # Back to normal

# Old outfits linked to new outfits (using the variable names)

init offset = 2 # Initialize chunk after character class and character outfits

default outfit_linking = {
    cc_party_slut_ITEM.id:          "cho_outfit_party",
    cc_muggle_hot_ITEM.id:          "cho_outfit_trainee",
    cc_outfit_sailor_white_ITEM.id: "cho_outfit_sailor",
    cc_costume_misty_ITEM.id:       "cho_outfit_misty",
    cc_japanese_school_uniform_ITEM.id: "cho_outfit_j_school",
    cc_bikini_micro_ITEM.id:        "cho_outfit_bikini",
    cc_lingerie_lace_ITEM.id:       "cho_outfit_lacelingerie",
    cc_dress_red_ITEM.id:           "cho_outfit_dress1",
    cc_smurfette_ITEM.id:           "cho_outfit_smurfette",
    ag_anntakamaki_ITEM.id:         "ast_outfit_ann",
    hg_bikini1.id:                  "her_outfit_bikini1",
    hg_bikini2.id:                  "her_outfit_bikini2",
    hg_maid.id:                     "her_outfit_maid",
    hg_bunny.id:                    "her_outfit_bunny",
    hg_ball.id:                     "her_outfit_ball",
    hg_yennefer.id:                 "her_outfit_yennefer",
    hg_bioshock.id:                 "her_outfit_bioshock",
    hg_swimsuit.id:                 "her_outfit_swimsuit",
    hg_poker.id:                    "her_outfit_poker",
    hg_egypt.id:                    "her_outfit_egypt",
    hg_latex_dress.id:              "her_outfit_latex_dress",
    hg_nightie.id:                  "her_outfit_nightie",
    hg_tifa.id:                     "her_outfit_tifa",
    hg_msmarv.id:                   "her_outfit_msmarv",
    hg_hslut.id:                    "her_outfit_hslut",
    hg_croft.id:                    "her_outfit_croft",
    hg_witch.id:                    "her_outfit_witch",
    hg_latex.id:                    "her_outfit_latex",
    hg_slutty_schoolgirl.id:        "her_outfit_slutty_schoolgirl",
    hg_teddy.id:                    "her_outfit_teddy",
    hg_fishnet.id:                  "her_outfit_fishnet",
    hg_bikini3.id:                  "her_outfit_bikini3",
    hg_cheerleader.id:              "her_outfit_cheerleader_1",
    hg_cheerleader2.id:             "her_outfit_cheerleader_2",
    nt_school.id:                   "ton_outfit_school",
    nt_casual.id:                   "ton_outfit_casual",
    nt_nightie.id:                  "ton_outfit_nightie",
    nt_bunny.id:                    "ton_outfit_bunny",
    nt_silky.id:                    "ton_outfit_silky",
    nt_bikini_1.id:                 "ton_outfit_bikini_1",
    nt_bikini_2.id:                 "ton_outfit_bikini_2",
    nt_bikini_3.id:                 "ton_outfit_bikini_3",
    nt_bikini_4.id:                 "ton_outfit_bikini_4"
}

init offset = 0 # back to normal
