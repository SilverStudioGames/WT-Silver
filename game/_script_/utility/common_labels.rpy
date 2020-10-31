# Hide all character images (not chibi)
label hide_characters:
    hide screen hermione_main
    hide screen luna_main
    hide screen cho_main
    hide screen astoria_main
    hide screen susan_main
    hide screen tonks_main
    hide screen snape_main
    hide screen genie_main
    # Do not add transitions. Use one after return.
    return

label hide_screens:
    # Remove all displayables on layer 'screens'
    $ renpy.scene("screens")
    return

label update_interface_color(color=None):
    if color in ["gold", "gray"]:
        $ interface_color = color
    elif not preferences.nightmode and daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"

    if interface_color == "gold":
        $ btn_hover = "#e3ba7140"
        $ interface_style = "day"
        $ menu_disabled = "#ae9566"
        $ daygold_colour = "{color=#000}"
        $ daygold_outline = [ (1, "#e4ba7080", 0, 0) ]
    else:
        $ btn_hover = "#7d75aa40"
        $ interface_style = "night"
        $ menu_disabled = "#6c625c"
        $ daygold_colour = "{color=#FFF}"
        $ daygold_outline = [ (1, "#00000080", 0, 0) ]
    return

label stop_sound_effects:
    stop bg_sounds fadeout 0.5
    stop weather fadeout 0.5
    return

# Reset menu
label reset_menu_position:

    $ menu_x = 0.5
    $ menu_y = 0.6

    return

label bld(action=None):
    if action == "hide":
        hide screen bld1
    else:
        show screen bld1
    with d3

    return

label blktone:
    show screen bld1 # blktone looks stupid without bld1
    show screen blktone
    with d5

    return

label hide_blktone:
    hide screen blktone
    with d5

    return

label blktone_top:
    show screen bld1 # blktone looks stupid without bld1
    show screen blktone5 # Has higher zorder than normal blktone
    with d5

    return

label hide_blktone_top:
    hide screen blktone5
    with d5

    return

label blkfade:
    hide screen bld1
    hide screen blktone
    show screen blkfade
    with d5
    pause.2

    return

label hide_blkfade:
    hide screen blkfade
    with d5

    return

label ctc:
    show screen ctc
    with d3
    pause
    hide screen ctc
    with d1

    return

label play_sound(sound=""):

    # Objects
    if sound in ["knock", "knocking"]: # knocking
        $ renpy.play('sounds/knocking.mp3')
    elif sound in ["knock2", "knocking2"]: # knocking
        $ renpy.play('sounds/knocking2.mp3')
    elif sound == "door":
        $ renpy.play('sounds/door.mp3')
    elif sound in ["lock","unlock"]: # lock
        $ renpy.play('sounds/09_lock.wav')
    elif sound in ["desk","climb_desk"]: # climb_desk
        $ renpy.play('sounds/08_hop_on_desk.mp3')
    elif sound == "owl":
        play sound "sounds/owl.mp3"

    # Ambience
    elif sound == "applause":
        $ renpy.play('sounds/applause01.ogg')

    # Affection
    elif sound in ["gulp", "gulping", "swallow", "swallowing"]: # gulp
        $ renpy.play('sounds/gulp.mp3')
    elif sound == "slap_1":
        $ renpy.play('sounds/slap.mp3')
    elif sound == "slap": # slap_2
        $ renpy.play('sounds/slap_02.mp3')
    elif sound == "slap_3":
        $ renpy.play('sounds/slap_03.mp3')
    elif sound in ["spit", "spitting"]: # spit
        $ renpy.play('sounds/spit.mp3')
    elif sound in ["kick", "kicking", "bump"]: # kick
        $ renpy.play('sounds/kick.ogg')
    elif sound in ["kiss", "kissing"]: # kiss
        $ renpy.play('sounds/kiss.mp3')
    elif sound in ["insert", "inserting", "goo"]: # insert
        $ renpy.play('sounds/gltch.mp3')
    elif sound == "boing":
        $ renpy.play('sounds/boing.mp3')
    elif sound in ["pop", "bottle"]: # pop
        $ renpy.play('sounds/bottle.mp3')
    elif sound == "snore":
        $ renpy.play('sounds/snore1.mp3')
    elif sound == "snore_quiet":
        $ renpy.play('sounds/snore2.mp3')
    elif sound == "snore_loud":
        $ renpy.play('sounds/snore3.mp3')
    elif sound == "giggle":
        $ renpy.sound.play("sounds/giggle2_loud.mp3")
    elif sound == "gasp":
        $ renpy.sound.play("sounds/MaleGasp.mp3")

    # Magic
    elif sound == "spell":
        $ renpy.play('sounds/magic2.mp3')
    elif sound == "morph":
        $ renpy.sound.play("sounds/magic3.mp3")
    elif sound == "magic":
        $ renpy.play('sounds/magic4.ogg')

    # Movement
    elif sound == "footsteps":
        $ renpy.play('sounds/footsteps.mp3')
    elif sound == "walking":
        $ renpy.play('sounds/run_04.mp3')
    elif sound == "running":
        $ renpy.play('sounds/run_03.mp3')
    elif sound == "sprinting":
        $ renpy.play('sounds/run_02.mp3')
    elif sound in ["walking_on_grass", "grass"]: # walking_grass
        $ renpy.play('sounds/steps_grass.mp3')

    # Interface
    elif sound == "scroll":
        $ renpy.play('sounds/scroll.mp3')
    elif sound in ["equip", "equip_inventory", "cloth"]: # equip
        $ renpy.play('sounds/cloth_sound.mp3')

    # Misc
    elif sound == "scratch":
        $ renpy.play('sounds/scratch.wav')
    elif sound == "shatter":
        $ renpy.play('sounds/glass_shatter.mp3')
    elif sound in ["glass_break","glass"]:
        $ renpy.play('sounds/glass_break.mp3')

    # Undefined sounds fallback
    elif renpy.loadable("sounds/{}.mp3".format(sound)):
        $ renpy.play("sounds/{}.mp3".format(sound))

    return

#TODO One keyword per theme (maybe define everything in a dictionary to simplify code further?)
label play_music(music=""):
    if music == "stop":
        stop music fadeout 1.0
        return

    # Harry Potter
    if music == "prologue":
        play music "music/01 Prologue.mp3" fadein 1 fadeout 1 if_changed
    elif music == "ball":
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 if_changed
    elif music == "festive":
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 if_changed
    elif music == "quidditch":
        play music "music/11 The Quidditch Match_original.mp3" fadein 1 fadeout 1 if_changed

    # Character Music
    elif music in ["snape", "dark_fog"]: # snape
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["hermione", "chipper_doodle"]: # hermione
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 if_changed
    elif music == "cho":
        play music "music/fuzzball-parade-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music == "astoria":
        play music "music/KMcL_OpenThoseBrightEyes.mp3" fadein 1 fadeout 1 if_changed
    elif music == "susan":
        play music "music/teddy-bear-waltz-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music == "tonks":
        play music "music/scheming-weasel-slower-version-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music == "luna":
        play music "music/wallpaper-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music == "playful_tension":
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 if_changed
    elif music == "silly":
        play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 if_changed

    # Store Music
    elif music == "weasley_store":
        play music "music/weasley_store.mp3" fadein 1 fadeout 1 if_changed
    elif music == "clothing_store":
        play music "music/clothing_store.mp3" fadein 1 fadeout 1 if_changed

    # Background Music
    elif music == "day":
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 if_changed
    elif music == "night":
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 if_changed
    elif music == "night_outside":
        play music "sounds/night.mp3" fadein 1 fadeout 1 if_changed
    elif music == "jazz":
        play music "sounds/jazz take 2.mp3" fadein 1 fadeout 1 if_changed

    # Interface
    elif music == "wardrobe":
        play music "music/Spring_In_My_Step.mp3" fadein 0.2 fadeout 0.2 if_changed

    # Misc
    elif music == "hitman":
        play music "music/hitman.mp3" fadein 1 fadeout 1 if_changed
    elif music == "boss":
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1 if_changed
    elif music == "cardgame":
        play music "music/Juhani_Junkala.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["sad","grape_soda"]: # sad
        play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 0.2 fadeout 0.5 if_changed
    elif music == "anguish":
        play music "music/Anguish.mp3" fadein 1 fadeout 1 if_changed
    elif music == "trance":
        play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 if_changed
    elif music == "despair":
        play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 if_changed
    elif music == "agenda":
        play music "music/hidden-agenda-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed

    # Fallback
    else:
        python:
            try:
                renpy.music.play(filenames="music/"+music+".mp3", channel="music", loop=True, fadeout=1.0, fadein=1.0)
            except IOError:
                if config.developer:
                    raise Exception("Music not found: {}".format(music))
    return

# Play day/night theme
label music_block:
    if daytime:
        call play_music("day")
    else:
        call play_music("night")
    return

label adjust_game_difficulty(dif=None):
    if 1 <= dif <= 3:
        $ game_difficulty = dif

    if game_difficulty <= 1:
        $ cheat_reading = True
        $ wine_ITEM.cost = 40
        $ firewhisky_ITEM.cost = 60
    elif game_difficulty == 2:
        $ cheat_reading = False
        $ wine_ITEM.cost = 60
        $ firewhisky_ITEM.cost = 80
    else:
        $ cheats_active = False
        $ cheat_reading = False
        $ wine_ITEM.cost = 140
        $ firewhisky_ITEM.cost = 160
    return

label unlock_clothing(text="", item="interface/icons/box_blue_1.webp"):

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    show screen clothing_unlock(item)
    show screen blktone5
    with d3

    menu:
        "[text]"
        "-Done Reading-":
            pass

    hide screen clothing_unlock
    hide screen blktone5
    with d3

    $ unlock_clothing_compat(item)

    call reset_menu_position

    return


label describe_mood(name, value):
    call blktone
    if 5 > value >= 1:
        ">[name] is a little upset with you..."
    elif 10 > value >= 5:
        ">[name] is upset with you."
    elif 20 > value >= 10:
        ">[name] is very upset with you."
    elif 30 > value >= 20:
        ">[name] is mad at you."
    elif 40 > value >= 30:
        ">[name] is very mad at you."
    elif 50 > value >= 40:
        ">[name] is furious at you."
    elif value >= 50:
        ">[name] hates your guts."
    else:
        ">[name] is calm."
    call hide_blktone

    return


label describe_mood_after_gift(was_negative, mood, change):
    if was_negative and mood == 0:
        call notes
        "She's no longer upset with you."
    elif was_negative and change < 0:
        "But she's still upset with you."
    elif was_negative:
        "She's still upset with you."

    return


label notes():
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    return
