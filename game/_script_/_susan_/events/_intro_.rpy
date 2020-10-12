
### Susan Intro ###

label nt_he_susan_E1:
    call ton_main(".................", "annoyed", "base", "shocked", "down", ypos="head")
    m "Something on your mind?"
    call ton_main("Yes, there's this student in my class. She seems to be having a bad time.", "open", "narrow", "worried", "mid")
    m "Education isn't meant to be enjoyable."
    call ton_main("It's not that, she's being bullied by the other students apparently...", "normal", "base", "worried", "R")
    m "Why is she being singled out?"
    call ton_main("For being shy... insecure...","upset","closed","base","mid")
    m "About what?"
    call ton_main("About her massive tits!", "open", "wide", "base", "mid")
    g4 "!!!"
    m "Why would she be insecure about that?"
    g9 "Surely that's something most girls would kill for!"
    call ton_main("That's what I said...", "open", "closed", "shocked", "mid")
    call ton_main("She didn't seem to think I was being genuine.", "soft", "base", "worried", "down")
    m "They're probably just jealous of her."
    call ton_main("Naturally... Even I'm jealous of those {b}milk-bags{/b} of hers!", "open", "shocked", "shocked", "mid")
    g9 "I definitely need to see them!"
    call ton_main("That being said, I'm quite worried about her...","open","closed","worried","mid")
    call ton_main("Lately she's been too shy to even answer the simplest of questions during my class.", "annoyed", "base", "worried", "R")
    call ton_main("She's lost quite a few points for her house that way.", "upset", "base", "worried", "mid")
    call ton_main("Not in my lessons, of course. I'd never take points from Hufflepuff!", "soft", "base", "worried", "R")
    g9 "Just send her my way and I'll drown her in house points!"
    m "And show her that her bod--"
    g4 "*Ahem!* Show her that she's appreciated..."
    call ton_main("That's what I was thinking...", "open", "closed", "base", "mid")
    g4 "Wait, you were?"
    call ton_main("Of course, why else would I be telling you about her?", "open", "wide", "annoyed", "mid")
    m "I don't know... banter?"
    m "Snape sure as hell hasn't sent me any girls..."
    call ton_main("I can teach him a thing or two about sharing - if you'd like...", "soft", "base", "annoyed", "mid")
    call ton_main("The more the merrier in my opinion...", "base", "happyCl", "base", "mid")
    m "You don't mean Snape and I..."
    call ton_main("Of course not, don't be silly!", "base", "narrow", "base", "mid")
    call ton_main("Maybe he's afraid you'd steal them from him if you got the chance...","horny","base","angry","mid")
    m "I have my doubts those girls he's talking about even exist..."
    m "But don't tell him I said that."
    call ton_main("I shall talk to Miss Bones.","open","closed","base","mid")

    if letter_min_favors.read:
        m "Bones... I think I've heard that name before..."
        call ton_main("Her Aunt works at the ministry.","open","base","base","mid")
        m "..."
    else:
        g9 "*He-He*... Bones."

    call ton_main("I'm sure you'll find her less than bony...","base","base","angry","mid")
    m "..."
    call ton_main("But, you have to promise me that you won't go overboard with her!", "mad", "base", "base", "mid")
    call ton_main("I'd rather not risk having her contact that aunt of hers...","open","base","base","R")
    m "I can be slick and subtle when I want to..."
    call ton_main("...","upset","base","worried","R")
    call ton_main("You're making me regret this decision already...","open","closed","worried","mid")

    ">As the hours pass, you convince Tonks to describe Susan's {b}massive tits{/b} to you..."
    ">You are glued to every word she has to say about them..."

    $ nt_he.susan_E1 = True
    $ sb_event_pause += 1 # New event the next day.

    jump end_tonks_hangout_points


label susan_intro_E1:
    stop music fadeout 1.0
    call play_sound("knocking")
    call bld
    "*knock-knock-knock*"

    who "*Ehm*... Professor Dumbledore, Sir?"
    who "May I come in?"
    m "Another girl?"

    $ d_flag_01 = False
    $ d_flag_02 = False

    menu:
        m "..."
        "\"Come on in.\"":
            who "Thank you, Sir."

        "\"Who's there?\"":
            $ d_flag_01 = True # Knows name.
            sus "Sus--{w=0.3} Susan Bones, Sir."
            g9 "Susan Bones who?"
            sus "... I'm sorry?"
            g9 "*Ha-ha-ha-ha!*"
            show screen blktone
            with d1
            m "I'm a terrible person..."
            hide screen blktone
            with d1
            sus "Professor?"
            m "Yes, please come on in..."
            sus "Thank you, Sir."

        "\"Not now.\"":
            $ d_flag_02 = True # Susan walks in anyway.
            who "Okay, Sir."

    call sus_walk(action="enter", xpos="mid", ypos="base")

    call bld
    if d_flag_02:
        g4 "Didn't I say not now--"
    else:
        m "How can I help you--"

    call play_music("susan")
    call sus_main("","base","base","base","mid", xpos="right", ypos="base")
    pause.8

    # Boing sound?
    call play_sound("boing")
    with hpunch
    g4 "(Damn! Look at them titties...)"

    menu:
        "\"Hello, Gorgeous!\"":
            call sus_main("*Ehm*...","upset","base","base","down") # Embarrassed.
            call sus_main("H-Hello...","open","base","worried","mid")

        "\"Susan! How great to see you!\"" if d_flag_01:
            g9 "Where have you been all my life?"
            call sus_main("I've been here at school for a couple of years now, Sir.","open","base","worried","R")

        "\"My day just got a whole lot brighter!\"":
            call sus_main("Sir?","upset","base","worried","mid")
            m "(Or should say darker?)"
            show screen blktone
            g9 "(Those tits must cast a huge-ass shadow...)"
            hide screen blktone

    call sus_main("Professor Tonks said you wanted to see me?","base","base","base","mid")
    g9 "Did she now?"
    m "(I have to get that woman a drink for introducing me to this magnificently voluptuous creature...)"
    g9 "Well, how nice of her."
    call sus_main("Is there anything I can help you with, Professor?","grin","base","base","mid")
    m "..."
    call sus_main("S-Sir?","open","base","worried","mid")
    m "(This must be that girl she wanted me to help with body confidence...)"
    m "Did professor Tonks tell you why I wanted to see you?"
    call sus_main("N-no...{w} I'm not in trouble am I?","upset","base","worried","down")
    m "Don't worry, I just needed to confirm something - You're free to go..."
    call sus_main("C-confirm something?","open","narrow","worried","mid")
    call sus_main("So I'm not in trouble then?","grin","base","base","mid")
    m "(This girl's got some confidence issues for sure...)"
    m "No miss Bones... You're not in any trouble."
    call sus_main("Very well...","base","base","base","mid")
    call sus_main("I shall return to my dormitory then.","open","base","base","R")
    call sus_main("Good--{w=0.4} Good day, Sir.","grin","base","base","mid")

    call sus_walk(action="leave")

    call bld
    m "..."
    m "Massive tits...{w=0.4} confirmed."

    $ susan_busy = True

    $ susan_unlocked = True
    $ achievement.unlock("unlocksus", True)
    call popup("{size=-4}You can now summon Susan into your office.{/size}", "Character unlocked!", "interface/icons/head/susan.webp")

    $ susan_intro.E1_complete = True
    $ ag_event_pause += 2 # Astoria intro starts in 2 days.

    jump main_room
