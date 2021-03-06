init python:
    def credits_title(title):
        return "{k=5.0}{size=+15}{outlinecolor=#842500}{color=#f9a001}{{" + title + "}{/color}{/outlinecolor}{/size}{/k}\n"

    def credits_group(*lines):
        return "".join(map(lambda x: "{k=1.5}"+x+"{/k}\n", lines))

define credits_text = "\n".join([
    "{image=logo/title.webp}{vspace=200}",
    credits_title("Director"),
    credits_group("MadMerlin"),
    credits_title("Artists"),
    credits_group("Soggy", "CyniclePickle", "DostojevskijSTG", "LoafyLemon", "Noodle", "perniciousducks"),
    credits_title("Writers"),
    credits_group("Johnny", "Mo"),
    credits_title("Programmers"),
    credits_group("Asease1", "LoafyLemon", "TropeCode"),
    credits_title("Music"),
    credits_group(
        "Harry Potter OST\n{size=-5}{color=#808080}{k=0.7}\"Prologue\"\n\"Shanghai Honey\"\n\"Introducing Colin\"\n\"Neville's Waltz\"\n\"The Quidditch Match\"{/k}{/color}{/size}\n",
        "Kevin MacLeod\n{size=-5}{color=#808080}{k=0.7}\"Anguish\"\n\"Awkward Meeting\"\n\"Brittle Rille\"\n\"Chipper Doodle v2\"\n\"Dark Fog\"\n\"Despair\"\n\"Game Over Theme\"\n\"Boss Theme\"\n\"Hitman\"\n\"Music for Manatees\"\n\"Plaint\"\n\"Fuzzball Parade\"\n\"Teddy Bear Waltz\"\n\"Scheming Weasel (Slower version)\"\n\"Open Those Bright Eyes\"\n\"Wallpaper\"\n\"Hidden Agenda\"{/k}{/color}{/size}\n",
        "PhobyAk\n{size=-5}{color=#808080}{k=0.7}\"Under-the-radar\"{/k}{/color}{/size}\n",
        "Shadow16nh\n{size=-5}{color=#808080}{k=0.7}\"Playful Tension (Orchestral)\"{/k}{/color}{/size}\n",
        "controllerhead\n{size=-5}{color=#808080}{k=0.7}\"Item Shop\"{/k}{/color}{/size}\n",
        "jrayteam6\n{size=-5}{color=#808080}{k=0.7}\"Grape Soda is Fucking Raw\"{/k}{/color}{/size}\n",
        "Juhani Junkala\n{size=-5}{color=#808080}{k=0.7}Retro Game Music Pack:\n\"Title Screen\"\n\"Level 1\"\n\"Level 3\"{/k}{/color}{/size}"
    ),
    credits_title("Special Thanks"),
    credits_group(
        "{size=+4}Akabur{/size}",
        "{color=#808080}{size=-5}{k=0.7}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}{/color}{/k}\n",
        "Dr. Lupin", "Lineup", "MaiL", "MedicBear", "STG Anon", "Boom313", "Sandmaster", "Pinguino", "UE Crew", "Catbug", "CaptainNemo", "Artguy", "Linear", "Amadan", "Anons", "Heretic", "Maverick", "Cleanzo", "Techy", "Zuel32", "Darwin7", "Ven"
    ),
"""{vspace=100}

Special thanks to our fans, discord moderators
and {a=https://www.patreon.com/SilverStudioGames/}patreon supporters{/a} {image=images/misc/heart.webp}

{image=logo/silverstudiogames.webp}
{vspace=100}

Thank you for playing!

{space=100}{image=characters/genie/mage9.webp}"""
])

define credits_duration = 30

define credits_chibis = (
    (Transform("ch_sna wand_defend", xzoom=-1), 1, 8, True),
    (Transform("ch_sna jerk_off", yoffset=120), 10, 6, False),
    ("ch_hem run", 12, 4, True),
    (Transform("hj", zoom=2, crop=(225,200,200,235)), 17, 5, True),
)

label credits:
    if not _menu:
        play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 noloop
    call hide_screens
    show screen credits(credits_text)
    with dissolve
    call update_interface_color("gray")
    $ achievement.unlock("Credits")
    pause credits_duration
    if not _menu:
        stop music fadeout 3
    call ctc
    hide screen credits
    with dissolve

    if _menu:
        # play music config.main_menu_music fadein 1 fadeout 3
        jump main_menu_screen
    else:
        return

transform credits_chibi_fade(start, duration):
    alpha 0
    pause start
    linear 0.5 alpha 1.0
    pause duration
    linear 0.5 alpha 0.0

screen credits(credits=credits_text, duration=credits_duration, chibis=credits_chibis):
    tag credits
    zorder 20

    add Solid("#000")

    for img, t, d, left in chibis:
        add img:
            at credits_chibi_fade(t, d)
            zoom 0.5
            if left:
                pos (20, config.screen_height - 20)
                align (0.0, 1.0)
            else:
                pos (config.screen_width - 20, config.screen_height - 20)
                align (1.0, 1.0)

    text credits:
        at transform:
            xalign 0.5
            yanchor 0.0
            ypos (config.screen_height / 2 - 125)
            pause 1
            parallel:
                linear (duration - 1) yanchor 1.0
            parallel:
                linear (duration - 1) ypos (config.screen_height + 50)
        xsize int(config.screen_width * 0.65)
        text_align 0.5
        color "#fff"
        outlines [(2, "#000", 0, 0)]
