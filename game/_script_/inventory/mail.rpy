default letter_queue_list = []
default report_money = 0
default deliveries = DeliveryQueue()

# Hermione Granger Letters
default letter_hg_1 = Letter(
    text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.{/size}\n\n{size=-7}With deepest respect,\nHermione Granger{/size}",
    label = "letter_from_hermione_A"
)

default letter_hg_2 = Letter(
    text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided in me... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.{/size}\n\n{size=-7}With deepest respect,\nHermione Granger.{/size}",
    label = "" # No comment on letter
)

default letter_nt_1 = Letter(
    text = "{size=-7}From: Tonks\nTo: My beloved headmaster\n\n{/size}{size=-4}As promised, here is a very lewd picture of me.{heart}\n\nI sincerely hope you received this letter before anybody had a chance to inspect the owl.\n\nIt would be shameful for me if this image was made public, and shared across all of Hogwarts...\nDon't you think so too, Professor?{heart}\n\nI had so much fun making this for you.\nPlease jerk off to it as much as you like! {heart} {heart} {heart}{/size}\n\n{size=-7}With love,\nTonks. {heart}{/size}",
    label = "letter_nt_1"
)

# Ministry of Magic Letters
default letter_min_work = Letter(
    text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nWe remind you that only upon providing us with a completed report will we be able to make a payment in your name.{/size}\n\n{size=-7}With deepest respect,\nThe Ministry of Magic.{/size}",
    label = "letter_paperwork_unlock"
)

default letter_min_report = Letter(
    text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n{/size}{size=-4}Thank you for completing a report this week.\n\nYou will find your payment of\n\n{/size}{b}-[report_money] gold-{/b}{size=-4}\n\nin the attached purse.{/size}\n\n{size=-7}With deepest respect,\nThe Ministry of Magic.{/size}",
    label = "letter_paperwork_report"
)

default letter_min_favors = Letter(
    text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nit has come to the ministry's attention from an anonymous letter, that there has been illicit activities going on between staff members and students within your halls.\n\nAn Auror has been dispatched and will arrive shortly to begin the investigation.{/size}\n\n{size=-7}Yours sincerely,\nAmelia Bones, Department of Magical Law Enforcement.{/size}",
    label = "letter_favor_complaint"
)

# Not in use anymore
default letter_min_curses = Letter(
    text = "{size=-7}Dear Albus Dumbledore, as we are sure you are aware, an unforgivable curse has been detected within the grounds of Hogwarts.\nWhile the punishment for such a curse is usually lifetime incarceration in the prison, Azkaban, we are allowing you to address this matter at your own discretion.\nThis is due to the possible nature of the spell being cast by a minor who has not fully grasped the serious nature of the curse.\nIf this is the case we expect no further communication from you regarding this unfortunate event.\nIf, however, you believe the curse has been cast by someone other than a student, or if any other complications arise we expect direct communication.\nLastly, the detection of any further curses will result in the immediate dispatchment of an auror to Hogwarts.\n\nCornelius Fudge,\nDepartment Head: Improper Use of Magic Office{/size}",
    label = "letter_curse_complaint"
)

# Card Game Letters
default letter_deck = Letter(
    text = "{size=-3}Sir Albus Dumbledore{/size}\n\n{size=-7}We would like to present to you great opportunity to become a Wizard Cards champion. We've included a starter pack to our card game in the hopes that you will consider any of our resellers to stock our cards for your students to purchase and play.\n\nHere's a little bit of information about our cards:\nEvery Wizard card has an enchantment that will personalise its look just for you and show something of your own favourite interest.\n\nDo you like Quidditch? Every card will look like a famous Quidditch player or a sport related print.\nInterested in magical creatures? The cards will have magical creatures on them.\nFind out your unique illustrations today with a starter pack, we don't even know what it is!{/size}\n\n{space=110}{size=-5}Wizard cards inc{/size}",
    label = "deck_mail_send"
)

default letter_cards_store = Letter(
    text = "{size=-7}Weasley's Wizard Wheezes shop emporium is now officially partnering with Wizard cards.\nCheck out the notice board at our shop to find a list of challengers at your skill level.{/size}",
    label = "cards_store_mail_send"
)

default letter_cardgame_t2 = Letter(
    text = "{size=-3}Congratulations!{/size}\n\n{size=-7}You've beaten your first 3 challenges of Wizard Cards.\nWe're currently working on expanding our business and are recruiting even more challengers so that in the future you'll be able to challenge even more people.\nIn the meanwhile, you'll be able to earn even more tokens by making wagers with the ones you've already beaten to complete your collection of items.\nFor wagers both participant needs to be fine with the prize/forfeit before the wager is made, good luck!\n\nYours truly,\nWeasley's Wizard Wheeze's and Team Silver{/size}",
    label = "cardgame_t2_mail_send"
)

label read_letter:

    if not always_read_letter:
        menu:
            "-Read Letter-":
                pass
            "-Shoo the bird away!-":
                jump shoo_owl_away

    $ letter = letter_queue_list[0]

    $ menu_x = 0.5
    $ menu_y = 0.9
    show screen bld1
    show screen blktone5
    show screen letter
    with d3

    menu:
        "-Done reading-":
            pass

    $ letter.read_letter()

    call reset_menu_position

    hide screen letter
    hide screen blktone5
    hide screen bld1
    with d3

    if letter.label != "":
        pause.2
        show screen bld1
        with d3

        $ renpy.call(letter.label)

        hide screen bld1
        with d3

    jump main_room


screen letter():
    zorder 20
    tag letter

    add "interface/letter.webp" pos (340, 30)
    hbox:
        spacing 40 pos (410, 80) xmaximum 250
        text letter.text

label shoo_owl_away:
    show screen chair_left
    show screen desk
    call gen_chibi("stand_alt", 420, 160+250, flip=False)
    with d5
    pause.2

    $ renpy.say(g4, renpy.random.choice(["fuck off", "bug off", "get out", "get the hell out of here", "go away", "away with you", "don't you even dare shit on my floor"])+", you"+renpy.random.choice([" stupid", " silly", " annoying", "", " idiotic", " bloody"])+renpy.random.choice([" flying rat!", " bird!", " poor excuse for a pigeon!", " pigeon!", " idiot!"]))
    pause.1

    call gen_chibi("rummage", 360, 80+349, flip=False)
    call play_sound("owl")
    hide screen owl
    with hpunch
    pause.8

    $ owl_away = True
    $ owl_away_counter += 1

    jump main_room

### Letter Attachment Call Labels ###

# Hermione Granger Letters.
label letter_from_hermione_A:
    m "Ehm........."
    m "What?"
    m "................................."

    return

# Ministry of Magic letters.
label letter_paperwork_unlock:
    m "Payments? Hmm..."

    call give_reward(">From now on you can do paperwork at your desk in order to earn additional gold...","interface/icons/gold.webp")
    call tutorial("workngold")

    return

label letter_paperwork_report:

    $ gold += report_money
    $ report_money = 0
    $ finished_report = 0

    return

label letter_favor_complaint:
    m "Amelia...{w=1.0} Bones?"
    g9 "*He-he-he-he-he*..."
    m "Wait a second..."
    m "Does that mean I'm in trouble?"
    return

label letter_nt_1:
    m "Well now I'm curious..."
    call nar(">You slowly roll out the piece of parchment.")
    pause.2
    call kiss_her
    pause.5

    m "Cute..."
    call play_sound("scroll")
    call nar(">You roll out the poster completely - getting a good look at it.")
    g9 "Nice!"

    call give_reward(text="{heart} {heart} {heart}", gift="interface/icons/posters/tonks.webp", sound=True)
    $ poster_tonks_ITEM.unlocked = True
    $ poster_tonks_ITEM.hidden = False

    g9 "I'll definitely hang this one up!"

    return

label update_report_money:

    if game_difficulty <= 1: # Easy
        $ report_money = finished_report * 50

    elif game_difficulty == 2: # Normal
        $ report_money = finished_report * 40

    else: # Hardcore
        $ report_money = finished_report * renpy.random.randint(20, 30)

    return

label letter_curse_complaint:
    m "That doesn't sound good..."
    m "Perhaps I should tell Snape about this."
    m "Or maybe miss granger?"

    return

### Mail about cardgame ###
label deck_mail_send:
    $ deck_unlocked = True

    m "That last bit just sounds like a scam to me..."
    m "..."
    m "I guess I'll have a look at the starter pack at least..."

    #Randomize starter pack (Hardcore difficulty gets randomized at the start of the game)
    if game_difficulty <= 2:
        python:
            card_rand_realm = random.choice([card_iris, card_jasmine, card_azalea])
            card_rand_girl = random.choice([card_her_schoolgirl, card_sus_schoolgirl, card_cho_schoolgirl, card_lun_schoolgirl])
            card_rand_item1 = random.choice([card_item_desk, card_item_bird])
            card_rand_item2 = random.choice([card_item_beads, card_item_dildo, card_item_doll, card_item_condoms, card_item_plugs])
            card_rand_item3 = random.choice([card_item_barbell, card_item_lingerie, card_item_stockings, card_item_badge, card_item_bdsm, card_item_lipstick])
            card_rand_item4 = random.choice([card_item_bookchairs, card_item_bookgala, card_item_bookgala2, card_item_bookwaifu, card_item_hat])
            card_rand_item5 = random.choice([card_item_eromag, card_item_pornmag, card_item_girlmag, card_item_scroll, card_item_wine, card_item_sweets])

            unlocked_cards = [card_genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2, card_rand_item3, card_rand_item4, card_rand_item5]
            playerdeck = [card_genie, card_rand_realm, card_rand_girl, card_rand_item1, card_rand_item2]
            # Delete copies of playerdeck cards
            for i in xrange(0,5):
                playerdeck[i].copies -= 1

    show screen blktone
    show screen start_deck
    with d3
    pause
    hide screen start_deck
    hide screen blktone
    with d3

    g9 "Hell yes I'm playing this..."
    call give_reward(">You've unlocked Wizard cards.\nUse the deck builder available on your desk to learn the rules and edit your deck.","interface/icons/cards.webp")

    return

### Twins card store unlocked ###
label cards_store_mail_send:
    $ twins_cards_stocked = True

    m "Great, let's see how they're doing."
    return

### Cardgame End of Content letter ###
label cardgame_t2_mail_send:
    #$ cardgame_eoc = True

    g9 "Sweet..."
    g9 "Fucking love prizes."
    $ advance_tier(2)

    return

label get_package:
    show screen blktone

    if clothing_mail_item != None:
        if clothing_mail_timer <= 0:
            call unlock_clothing(text="You have received a new outfit.",item=clothing_mail_item)
            $ clothing_mail_item = None
            $ clothing_mail_timer = 0

    python:
        gift_list = []
        for item in deliveries.get_mail():
            if item.type == 'Event_item':
                pass

            if item.type == 'Gift':
                gift = item.item
                gift.number += item.quantity
                gift_list.append([gift.name, gift.get_image(), item.quantity])

        if len(gift_list) > 0:
            renpy.block_rollback()
            if len(gift_list) == 1:
                if gift_list[0][2] == 1:
                    renpy.call("give_reward","You have received "+gift_list[0][0]+".", gift_list[0][1])
                else:
                    renpy.call("give_reward","You have received "+str(gift_list[0][2])+" pieces of "+gift_list[0][0]+".", gift_list[0][1])
            else:
                txt_gifts = "{size=-4}"
                for i, item in enumerate(gift_list):
                    if i < len(gift_list)-1:
                        txt_gifts += str(item[2])+" "+item[0]+", "
                    else:
                        txt_gifts += str(item[2])+" "+item[0]+".{/size}"
                renpy.block_rollback()
                renpy.call("give_reward","You have received your ordered items:\n"+txt_gifts, "interface/icons/box_brown_"+str(random.randint(1, 4))+".webp")

    hide screen package
    hide screen blktone
    with d3

    $ package_is_here = False
    $ renpy.block_rollback()

    call tutorial("inventory")

    jump main_room_menu

init python:

    class DeliveryItem(object):
        def __init__(self, item, transit_time, quantity,type):
            self.item = item
            self.transit_time = transit_time
            self.quantity = quantity
            self.type = type

    class DeliveryQueue(object):
        max_wait = 15

        def __init__(self):
            self.queue = []

        def send(self, item, transit_time, quantity, type):
            if transit_time > self.max_wait:
                transit_time = self.max_wait
            self.queue.append(DeliveryItem(item, transit_time, quantity, type))

        def got_mail(self):
            for i in self.queue:
                i.transit_time -= 1
            for i in self.queue:
                if i.transit_time <= 0:
                    return True
            return False

        def get_mail(self):
            delivery = []
            for i in list(self.queue):
                if i.transit_time <= 0:
                    delivery.append(i)
                    self.queue.remove(i)
            return delivery

    class Letter(object):

        def __init__(self, **kwargs):
            self.mailed = False
            self.read = False
            self.text = "Add Text"
            self.label = ""

            self.__dict__.update(**kwargs)

        def send_letter(self):
            self.mailed = True
            self.read = False
            if self not in letter_queue_list:
                letter_queue_list.append(self)
            return

        def read_letter(self):
            self.read = True
            if self in letter_queue_list:
                letter_queue_list.remove(self)
            return
