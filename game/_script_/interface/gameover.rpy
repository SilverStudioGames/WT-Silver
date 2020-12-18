label gameover(fake=False):

    # Fade to black
    $ renpy.pause(0.5, hard=True)

    hide screen cartoon_zoom
    show screen gameover
    hide screen blkfade
    with d9

    $ renpy.pause(0.5, hard=True)
    $ renpy.play('sounds/jail_door.mp3')
    $ renpy.pause(1.2, hard=True)
    with hpunch
    $ renpy.pause(1.3, hard=True)
    $ renpy.play('sounds/killswitch_on.mp3')
    $ renpy.pause(4.0, hard=True)
    if fake:
        show screen blkfade
        with d9

        $ renpy.pause(0.9, hard=True)

        play music "music/Only 115 (Electro Loop)_125 BPM.mp3" fadein 0.5 fadeout 1

        hide screen gameover
        hide screen blkfade
        show screen credits(fake_credits_text, 30)
        with blinds

        $ renpy.pause(12, hard=True)

        hide screen credits
        with None

    hide screen gameover
    return

define fake_credits_text = "\n".join([
    "{image=logo/title.webp}{vspace=200}",
    credits_title("Director"),
    credits_group("The Orchestrator of Sex"),
    credits_title("Artists"),
    credits_group("A Professional Pervert", "The Purveyor of Pencils", "The Deviant Drawer", "A Painter of Filth"),
    credits_title("Writers"),
    credits_group("The Scribbler of smut", "The Lore keeper of Whores"),
    credits_title("Programmers"),
    credits_group("The Engineer of ecstasy", "A Tits Techie", "A guy that gets erect from calculator spelling boobs"),
    credits_title("Music"),
    credits_group(
        "Happy Rooster OST\n{size=-5}{color=#808080}{k=0.7}\"Shanghai Honey\"\n\"Introducing Colin\"{/k}{/color}{/size}\n",
        "Music Dude#1\n{size=-5}{color=#808080}{k=0.7}\"Anguish\"\n\"Awkward Meeting\"\n\"Brittle Rille\"\n\"Chipper Doodle v2\"\n\"Dark Fog\"\n\"Despair\"\n\"Game Over Theme\"\n\"Boss Theme\"\n\"Hitman\"\n\"Music for Manatees\"\n\"Plaint\"\n\"Fuzzball Parade\"\n\"Teddy Bear Waltz\"\n\"Scheming Weasel (Slower version)\"\n\"Open Those Bright Eyes\"{/k}{/color}{/size}\n",
        "Music Dude#2\n{size=-5}{color=#808080}{k=0.7}\"Under-the-radar\"{/k}{/color}{/size}\n",
        "Music Dude#3\n{size=-5}{color=#808080}{k=0.7}\"Playful Tension (Orchestral)\"{/k}{/color}{/size}\n",
        "Music Dude#4\n{size=-5}{color=#808080}{k=0.7}\"Item Shop\"{/k}{/color}{/size}\n",
        "Music Dude#5\n{size=-5}{color=#808080}{k=0.7}\"Grape Soda is Fucking Raw\"{/k}{/color}{/size}\n",
        "Music Dude#5\n{size=-5}{color=#808080}{k=0.7}Retro Game Music Pack:\n\"Title Screen\"\n\"Level 1\"\n\"Level 3\"{/k}{/color}{/size}"
    ),
    credits_title("Special Thanks"),
    credits_group("{size=+4}Pervert#1{/size}\n{color=#808080}{size=-5}{k=0.7}Creator of the original Witch Trainer and other awesome games! {a=https://www.patreon.com/akabur}PATREON{/a}{/size}{/color}\n{/k}", "Pervert#2", "Pervert#3", "Pervert#4", "Pervert#5", "Pervert#6", "Pervert#7", "Pervert#8", "Pervert#9", "Pervert#10", "Pervert#11", "Pervert#12", "Pervert#13", "Pervert#14", "Pervert#15", "Pervert#16", "Pervert#17", "Pervert#18", "Pervert#19", "Pervert#20", "Pervert#21"),
    "\nSpecial thanks to our pervs, discord perverators and {a=https://www.patreon.com/SilverStudioGames/}perverted supporters{/a} {image=images/misc/heart.webp}\n\n",
    "{image=logo/silverstudiogames.webp}\n"
    "\n{space=220}{image=characters/genie/mage9.webp}{rb}{space=-60}Thanks for cumin!{/rb}"
])

screen cartoon_zoom():
    tag gameover
    zorder 31 # Above saybox

    button style "empty" action NullAction()

    add "images/misc/circle_cartoon.webp":
        at transform:
            xanchor 0.1
            yanchor 0.9
            xpos 108
            ypos 540
            yoffset 1300
            xzoom 24.0
            yzoom 24.0
            easein_quart 5.0 xzoom 1.0 yzoom 1.0 yoffset 0

    add Solid("#000000"):
        at transform:
            alpha 0.0
            pause 5.0
            linear 1.0 alpha 1.0

screen gameover():
    tag gameover
    zorder 20

    button style "empty" action NullAction()

    add Solid("#000000")
    add "images/misc/gameover.webp":
        at transform:
            alpha 0.0
            pause 1.0
            linear 2.0 alpha 1.0
    add Solid("#000000"):
        at transform:
            alpha 0.5
            pause 4.8
            alpha 0.0
    add "images/misc/light.webp":
        at transform:
            alpha 0.0
            pause 4.8
            alpha 1.0

    add "images/misc/folks.webp":
        at transform:
            alpha 0.0
            pause 4.8
            alpha 1.0
