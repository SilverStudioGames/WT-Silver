default tutorial_dict = {"hearts": ["{heart} Hearts System", "Hearts indicate your current status towards a personal favour.\n\n{color=#FFFFFF80}{b}Empty Heart{/b}{/color}{size=-2} indicates the event hasn't been seen yet.{/size}\n{color=#bf5649}{b}Red Heart{/b}{/color}{size=-2} indicates completion of the event.{/size}\n{color=#333333}{b}Black Heart{/b}{/color}{size=-2} indicates failure of the event and you should try it again at a higher character level.{/size}\n{b}{color=#FFFFFF80}Half{/color} {color=#bf5649}Heart{/color}{/b}{size=-2} indicates there's a hidden path inside the event you should follow, in order to progress further.{/size}", False],
"moodngifts": ["Mood & Gifts", "Sometimes your choices may upset some characters, just like in life. You can try and avoid picking options that you think would upset them, but if you mess up, buy them some nice {color=#204997}{b}gift{/b}{/color} and they might forgive you. Keep in mind that every character has their own gift preferences.\n\nAlternatively, you can wait until they calm down but who knows how long that would take.", False],
"hangouts": ["Hangouts", "Getting to know your accomplices is an important aspect of progressing through the game. Hanging out with Snape for example improves your friendship and support which has various benefits such as story and character related unlockables.\n\nYou can check your current relationship status in the {color=#204997}{b}characters menu{/b}{/color}. It is accessible by clicking the heart button or by pressing {color=#204997}{b}C{/b}{/color} key.", False],
"workngold": ["Working & Gold", "Gold is a universal currency in the magical world. To earn gold you must complete at least one full report for the ministry. You can start working by clicking on the {color=#204997}{b}work button{/b}{/color}, clicking on the desk and papers or by pressing {color=#204997}{b}W{/b}{/color} key.\n\nYou might find other work opportunities as you progress through the game.", False],
"inventory": ["Inventory & Items", "The inventory screen allows you to examine items you possess. You can access it by clicking on the {color=#204997}{b}inventory button{/b}{/color} located on the top right part of the screen, or by pressing the  {color=#204997}{b}I{/b}{/color} key. The inventory is split into two main categories:\n{color=#204997}{b}Gifts{/b}{/color} - Items that can be given to other characters.\n{color=#204997}{b}Quest Items{/b}{/color} - Important items related to game progression. Some of them can be used by clicking on the {b}USE{/b} button next to the item name when it's selected.", False],
"schedule": ["Outfits Schedule", "Outfits can be assigned into a set schedule, which will allow the girls to pick what they are going to wear next time you summon them, based on time of day and weather conditions.\n\nYou can assign schedules inside the Wardrobe's Outfits Manager section, by clicking on the icon represented above. \n\nThis feature can be disabled at any time in the wardrobe.", False]}

init python:
    def tutorial_is_done(entry):
        return tutorial_dict[entry][2]

label tutorial(entry):
    if not tutorial_dict[entry][2] and preferences.tutorials == True:
        $ tutorial_dict[entry][2] = True
        $ screenshot_image = ScreenshotImage.capture()
        $ renpy.play("sounds/pop01.mp3")
        $ renpy.music.set_volume(0.5, 3.0)
        $ renpy.call_in_new_context("tutorial.display", entry)
        $ renpy.music.set_volume(1.0, 3.0)
    return

    label .display(entry):
        show screen tutorial(entry)

        $ _return = ui.interact()

        return

screen tutorial(entry):
    $ _style = ("day_button" if interface_color == "gold" else "night_button")
    $ _bg = ("#ac8d5a" if interface_color == "gold" else "#5d5151")

    default bg = At(screenshot_image, gaussianblur(15.0))
    add bg

    frame:
        background _bg
        xysize (500, 300)
        align (0.5, 0.5)

        add "interface/achievements/"+interface_color+"/highlight.webp" yoffset -2
        add "interface/achievements/"+interface_color+"/spacer.webp" xalign 0.5 ypos 17

        text "Tutorial" size 10 ypos 3

        vbox:
            spacing 5

            text tutorial_dict[entry][0] size 16 xalign 0.5

            if renpy.loadable("interface/tutorials/{}.webp".format(entry)):
                add "interface/tutorials/{}.webp".format(entry) xalign 0.5

            text tutorial_dict[entry][1] size 12

        textbutton "Ok" align (1.0, 1.0) action Return(True) style _style
