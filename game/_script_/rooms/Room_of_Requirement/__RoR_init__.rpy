default mirror_intro_done = False

default mr_ev_WPIIA = MirrorStory(
    name = "Whose points is it anyway?",
    unlockable = True,
    story_description = "Parody of the game show of \"whose points is it anyway?\"",
    start_label = "whose_points",
    authors = ["TeamSilver"],
    categories= ["Parody","Lewd", "Gameshow"],
    ach_desc = "Unlock the characters",
    content_characters = ["luna", "astoria", "hermione"]
)
default mr_ev_GHE = MirrorStory(
    name = "The genie, the desk and the door",
    story_description = "The genie tries to figure out how people know when he calls for them.",
    start_label = "genie_house_elf",
    authors = ["TeamSilver"],
    categories= ["Parody"],
    ach_desc = "Unlock the mirror of noisrevrep/Erised",
    content_characters = []
)
default mr_ev_AOC = MirrorStory(
    name = "An odd circumstance",
    unlockable = True,
    story_description = "You find yourself being confronted by a mysterious girl that seemingly seems to know you.",
    start_label = "an_odd_circumstance",
    authors = ["TeamSilver"],
    categories= ["Parody", "lewd"],
    ach_desc = "Completed Hermione's Suck It personal favours",
    content_characters = ["hermione"]
)
default mr_ev_ABTTD = MirrorStory(
    name = "A bad time to disrobe",
    unlockable = True,
    story_description = "The genie gets a hold of a invisibility cloak and puts it to good use.",
    start_label = "a_bad_time_to_disrobe",
    authors = ["TeamSilver"],
    categories= [],
    ach_desc = "Finish private favour, \"Show them to me!\" at least once.",
    content_characters = ["hermione"]
)
default mr_ev_ASOC = MirrorStory(
    name = "A spaced out conversation",
    unlockable = True,
    story_description = "The genie and Snape gets real for a little bit.",
    start_label = "a_spaced_out_conversation",
    authors = ["Ignatz"],
    categories= [],
    ach_desc = "Unlocks after spending some evenings drinking by the fire with Snape.",
    content_characters = []
)
default mr_ev_ABAS = MirrorStory(
    name = "A Booty at sea",
    unlockable = True,
    story_description = "The genie imagine himself to be a great pirate and roleplays his most intimate times with Hermione.",
    start_label = "anal_pirate_event",
    authors = ["TeamSilver"],
    categories= [],
    ach_desc = "Finish the \"Time for Anal\" Private favours.",
    content_characters = ["hermione"]
)
default mr_ev_ADR = MirrorStory(
    name = "A Dark Room (Incomplete)",
    story_description = "A minigame inspired by the text-based game \"A Dark Room\".\n>WIP! It is currently incomplete but in a playable state.",
    start_label = "start_dark_room_game",
    authors = ["TeamSilver"],
    categories= ["minigame"],
    ach_desc = "",
    content_characters = []
)
default mr_ev_AXmasTale = MirrorStory(
    name = "A Christmas Tale",
    story_description = "A surprise visit.",
    start_label = "a_christmas_tale",
    authors = ["TeamSilver"],
    categories= [],
    ach_desc = "",
    content_characters = []
)
default mr_ev_AXmasTale2 = MirrorStory(
    name = "Santa's Little Helper",
    story_description = "Tall broody guy is about to get his present.",
    start_label = "a_christmas_tale2",
    authors = ["TeamSilver"],
    categories= [],
    ach_desc = "",
    content_characters = []
)
# Story Unlock requirements: Finish the first 3 Wizard Cards challenges.
default mr_ev_PaH = MirrorStory(
    name = "Previously at Hogwarts",
    story_description = "Snape tries to find a solution to stifle his anger and finds himself yet again in the headmaster's office.",
    start_label = "prev_at_hogwarts",
    authors = ["TeamSilver"],
    categories= [],
    ach_desc = "",
    content_characters = []
)
default mr_ev_PR = MirrorStory(
    name = "Panty Raid",
    unlockable = True,
    story_description = "Genie asks Hermione to go out and collect other girls panties.",
    start_label = "panty_raid",
    authors = ["WaxerRed"],
    categories= ["Panties fetish", "Lesbian", "Corruption"],
    ach_desc = "",
    content_characters = ["hermione"]
)

default mr_ev_EFP = MirrorStory(
    name = "Eating for pleasure",
    story_description = "You get hungry and decide to get something to eat.",
    start_label = "eating_for_pleasure",
    authors = ["TeamSilver"],
    categories= ["Food fetish", "Call girl", "Parody"],
    ach_desc = "",
    content_characters = ["hermione"]
)

default mr_ev_SNR = MirrorStory(
    name = "Suck & Run",
    story_description = "Someone or {i}something{/i} is sucking out the life force out of the students.",
    start_label = "suck_and_run",
    authors = ["TeamSilver"],
    categories= ["Spooky", "Blowjob", "Reverse Corruption"],
    ach_desc = "",
    content_characters = ["tonks", "snape"]
)

default mr_evs_list = [
    mr_ev_SNR,
    mr_ev_PaH,
    mr_ev_AXmasTale,
    mr_ev_AXmasTale2,
    mr_ev_WPIIA,
    mr_ev_GHE,
    mr_ev_ABTTD,
    mr_ev_ASOC,
    mr_ev_ABAS,
    mr_ev_PR,
    mr_ev_AOC,
    mr_ev_EFP,
]

default current_page = 0

init python:

    class MirrorStory(object): # This class extends Item only so it can be displayed in the item menu screen (refactor?)

        def __init__(self, **kwargs):
            self.start_label = ""
            self.authors = []
            self.categories = []
            self.story_description = ""
            self.ach_desc = ""
            self.content_characters = []

        def get_name(self):
            ret_str = "{size=-2}\""+self.name+"\"{/size}{size=-6} by "
            for s in self.authors:
                ret_str += s +", "

            return ret_str[0:len(ret_str)-2]+"{/size}"

        def get_description(self):
            if self.unlocked:
                return self.story_description
            else:
                return self.ach_desc

        def get_annotation(self):
            ret_str = ""
            for c in self.content_characters:
                if c == "luna":
                    ret_str += "{image=interface/room_of_req/luna_icon.webp}"
                elif c == "hermione":
                    ret_str += "{image=interface/room_of_req/hermione_icon.webp}"
                elif c == "astoria":
                    ret_str += "{image=interface/room_of_req/astoria_icon.webp}"
                elif c == "susan":
                    ret_str += "{image=interface/room_of_req/susan_icon.webp}"
                elif c == "cho":
                    ret_str += "{image=interface/room_of_req/cho_icon.webp}"
                elif c == "tonks":
                    ret_str += "{image=interface/room_of_req/tonks_icon.webp}"

            return ret_str

        def get_image(self):
            if self.unlocked:
                return Image("interface/unlocked_True.webp")
            else:
                return Image("interface/unlocked_False.webp")

        def check_lock(self):
            unlocked = True
            for c in self.content_characters:
                if c == "luna":
                    unlocked = unlocked and luna_unlocked
                elif c == "hermione":
                    unlocked = unlocked and hermione_unlocked
                elif c == "astoria":
                    unlocked = unlocked and astoria_unlocked
                elif c == "susan":
                    unlocked = unlocked and susan_unlocked
                elif c == "cho":
                    unlocked = unlocked and cho_unlocked
                elif c == "tonks":
                    unlocked = unlocked and tonks_unlocked
                else:
                    unlocked = False
            self.unlocked = unlocked and self.unlock_check()
            if self.unlocked:
                self.unlockable = False # Makes item clickable
            return self.unlocked

        def unlock_check(self):
            # Add elif with the name and the condition to unlock,
            # otherwise it will always be unlocked
            if self.name == "A bad time to disrobe":
                return hg_pf_admire_breasts.tier > 1
            elif self.name == "A spaced out conversation":
                return sna_friendship > 60
            elif self.name == "A Booty at sea":
                return hg_anal.trigger == True
            elif self.name == "An odd circumstance":
                return hg_blowjob.trigger == True
            elif self.name == "Panty Raid":
                return her_whoring > 20 #TODO Maybe unlock this at lower whoring/level (or use 'jerk off with panties' as a trigger?)
            else:
                return True
