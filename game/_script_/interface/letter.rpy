
### Init ###

# Hermione Granger Letters
default letter_hg_1 = Letter(
    text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.{/size}\n\n{size=-7}With deepest respect,\nHermione Granger{/size}"
)

default letter_hg_2 = Letter(
    text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided in me... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.{/size}\n\n{size=-7}With deepest respect,\nHermione Granger.{/size}",
    label = "letter_hg_2",
    wait = 2,
)

label letter_hg_2:
    m "This again?"
    m "..........."
    return

# Ministry of Magic Letters
default letter_work_unlock = Letter(
    text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nWe remind you that only upon providing us with a completed report will we be able to make a payment in your name.{/size}\n\n{size=-7}With deepest respect,\nThe Ministry of Magic.{/size}",
    label = "letter_work_unlock",
    wait = 4,
)

label letter_work_unlock:
    m "Payments? Hmm..."
    call give_reward(">From now on you can do paperwork at your desk in order to earn additional gold...","interface/icons/gold.webp")
    call tutorial("workngold")
    return

default letter_work_report = Letter(
    text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n{/size}{size=-4}Thank you for completing a report this week.\n\nYou will find your payment of\n\n{/size}{b}-[reports_gold] gold-{/b}{size=-4}\n\nin the attached purse.{/size}\n\n{size=-7}With deepest respect,\nThe Ministry of Magic.{/size}",
    label = "letter_work_report",
    func = calc_reports_gold
)

init python:
    def calc_reports_gold():
        global reports_gold, reports_finished

        if game.difficulty <= 1: # Easy
            reports_gold = reports_finished * 50
        elif game.difficulty == 2: # Normal
            reports_gold = reports_finished * 40
        else: # Hardcore
            reports_gold = reports_finished * renpy.random.randint(20, 30)

label letter_work_report:
    python:
        game.gold += reports_gold

        # Reset
        reports_finished = 0
        reports_gold = 0
    return

default letter_favors = Letter(
    text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore,\nit has come to the ministry's attention from an anonymous letter, that there has been illicit activities going on between staff members and students within your halls.\n\nAn Auror has been dispatched and will arrive shortly to begin the investigation.{/size}\n\n{size=-7}Yours sincerely,\nAmelia Bones, Department of Magical Law Enforcement.{/size}",
    label = "letter_favors",
    wait = 7,
)

label letter_favors:
    m "Amelia...{w=1.0} Bones?"
    g9 "*He-he-he-he-he*..."
    m "Wait a second..."
    m "Does that mean I'm in trouble?"
    return

# Card Game Letters
default letter_cards_unlock = Letter(
    text = "{size=-3}Sir Albus Dumbledore{/size}\n\n{size=-7}We would like to present to you great opportunity to become a Wizard Cards champion. We've included a starter pack to our card game in the hopes that you will consider any of our resellers to stock our cards for your students to purchase and play.\n\nHere's a little bit of information about our cards:\nEvery Wizard card has an enchantment that will personalise its look just for you and show something of your own favourite interest.\n\nDo you like Quidditch? Every card will look like a famous Quidditch player or a sport related print.\nInterested in magical creatures? The cards will have magical creatures on them.\nFind out your unique illustrations today with a starter pack, we don't even know what it is!{/size}\n\n{space=110}{size=-5}Wizard cards inc{/size}",
    label = "letter_cards_unlock",
    wait = 24
)

label letter_cards_unlock:
    $ deck_unlocked = True

    m "That last bit just sounds like a scam to me..."
    m "..."
    m "I guess I'll have a look at the starter pack at least..."

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

default letter_cards_store = Letter(
    text = "{size=-7}Weasley's Wizard Wheezes shop emporium is now officially partnering with Wizard cards.\nCheck out the notice board at our shop to find a list of challengers at your skill level.{/size}",
    label = "letter_cards_store"
)

label letter_cards_store:
    $ twins_cards_stocked = True
    m "Great, let's see how they're doing."
    return

default letter_cards_tier2 = Letter(
    text = "{size=-3}Congratulations!{/size}\n\n{size=-7}You've beaten your first 3 challenges of Wizard Cards.\nWe're currently working on expanding our business and are recruiting even more challengers so that in the future you'll be able to challenge even more people.\nIn the meanwhile, you'll be able to earn even more tokens by making wagers with the ones you've already beaten to complete your collection of items.\nFor wagers both participant needs to be fine with the prize/forfeit before the wager is made, good luck!\n\nYours truly,\nWeasley's Wizard Wheeze's and Team Silver{/size}",
    label = "letter_cards_tier2"
)

label letter_cards_tier2:
    g9 "Sweet..."
    g9 "Fucking love prizes."
    $ advance_tier(2)

    return

# Tonks
default letter_nt_1 = Letter(
    text = "{size=-7}From: Tonks\nTo: My beloved headmaster\n\n{/size}{size=-4}As promised, here is a very lewd picture of me.{heart}\n\nI sincerely hope you received this letter before anybody had a chance to inspect the owl.\n\nIt would be shameful for me if this image was made public, and shared across all of Hogwarts...\nDon't you think so too, Professor?{heart}\n\nI had so much fun making this for you.\nPlease jerk off to it as much as you like! {heart} {heart} {heart}{/size}\n\n{size=-7}With love,\nTonks. {heart}{/size}",
    label = "letter_nt_1"
)

label letter_nt_1:
    m "Well now I'm curious..."
    call nar(">You slowly roll out the piece of parchment.")
    pause.2
    call kiss_her
    pause.5

    m "Cute..."
    call play_sound("scroll")
    call nar(">You roll out the poster completely - getting a good look of it.")
    g9 "Nice!"

    call give_reward(text="{heart} {heart} {heart}", gift="interface/icons/tonks_poster.webp", sound=True)
    $ poster_tonks_ITEM.unlocked = True
    $ poster_tonks_ITEM.hidden = False

    g9 "I'll definitely hang this one up!"

    return

### Main ###

init python:
    class Letter(object):
        """
        text - Contents of the letter.
        label - Call label called after the letter was read.
        func - A setup function called before the letter is being shown to the player.

        Queue is universal for all instanced objects.
        """

        def __init__(self, text="Add Text", wait=0, label=None, func=None):
            self.mailed = False
            self.read = False
            self.text = text
            self.wait = wait
            self.label = label
            self.func = func
            self.queue = mailbox.letters

        def send(self):
            self.mailed = True

            if not self in self.queue:
                self.queue.append(self)

        def open(self, silent=False):
            self.mailed = True
            self.read = True

            if self in self.queue:
                self.queue.remove(self)

            if self.func:
                self.func()

            if not silent:
                renpy.call("letter", self.text, self.label)

label letter(text, label):
    show screen bld1
    show screen blktone
    show screen letter(text)
    with d3

    $ menu_x, menu_y = 0.5, 0.9

    menu:
        "-Done reading-":
            pass

    call reset_menu_position

    hide screen letter
    hide screen blktone
    hide screen bld1
    with d3

    if label:
        $ renpy.call(label)

    return

screen letter(text):
    zorder 20
    tag letter

    add "interface/letter.webp" align (0.5, 0.2) zoom 0.5
    hbox:
        spacing 40
        pos (410, 80)
        xmaximum 250
        text text

label letter_open_all:
    while mailbox.get_letters():
        $ mailbox.get_letters()[0].open()

    $ owl_OBJ.hidden = True

    jump main_room_menu

label letter_delay:
    call gen_chibi("stand_alt", 420, 410, flip=False)
    with d5
    pause.2

    $ renpy.say(g4, renpy.random.choice(["fuck off", "bug off", "get out", "get the hell out of here", "go away", "away with you", "don't you even dare shit on my floor"])+", you"+renpy.random.choice([" stupid", " silly", " annoying", "", " idiotic", " bloody"])+renpy.random.choice([" flying rat!", " bird!", " poor excuse for a pigeon!", " pigeon!", " idiot!"]))
    pause.1

    call gen_chibi("rummage", 360, 429, flip=False)
    call play_sound("owl")
    $ owl_OBJ.hidden = True
    with hpunch
    pause.8

    $ owl_away = True
    $ owl_away_counter += 1

    jump main_room
