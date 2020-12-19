
# Mirror story: A bad time to disrobe
label a_bad_time_to_disrobe:

    # Setup
    $ temp_day = daytime

    stop weather
    call play_music("stop")
    call room("main_room")
    hide screen owl
    show screen blkfade
    with d5

    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_default)

    centered "{size=+7}{color=#cbcbcb}A bad time to disrobe{/color}{/size}"

    nar "In this story the genie has found an invisibility cloak."
    nar "And with the cloak come great opportunities."

    menu:
        "-Part 1-":
            jump a_bad_time_to_disrobe_part_1
        "-Part 2-":
            jump a_bad_time_to_disrobe_part_2


label a_bad_time_to_disrobe_part_1:

    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d5

    call music_block
    call bld
    m "Miss Granger. Have you ever been excited about the thought of being caught?"

    call her_main("Caught?", "soft", "base", "base", "mid", xpos="right",ypos="base", trans=d3)
    call her_main("In what way professor?", "base", "base", "base", "mid")

    m "Well, for today's favour I have a prop for you to use."

    call her_main("A prop sir?", "base", "base", "base", "mid")

    m "Yes, I'd like you to put this invisibility cloak on and sneak into one of the boy only areas of the school."

    call her_main("Well, I guess that would be fine...", "base", "base", "base", "mid")
    call her_main("Seems a bit different than your usual requests.", "soft", "base", "base", "R", cheeks="blush")

    m "You'd be naked of course."

    call her_main("Naked!?! But what if someone saw me?", "open", "wide", "base", "stare")

    m "You'll be wearing the cloak..."
    m "No one would even know you were there."

    call her_main("{size=-7}Thirty-five points...{/size}", "annoyed", "closed", "angry", "mid")

    m "Twenty-five points you said? sounds good to me."

    call her_walk("door", "base")

    call her_main("{size=-7}You heard what I said...{/size}", "annoyed", "closed", "base", "mid", flip=True, trans=d3)
    call her_chibi("leave")

    g9 "\"Some of that bartering skill put to good use...\""

    show screen day_to_night
    with d3

    $ daytime = False
    call update_interface_color
    call music_block

    nar "Later that evening. Hermione returns."
    call her_chibi("stand","desk","base")

    hide screen day_to_night
    with d3

    call bld
    g9 "I'll take that cloak back if you don't mind."
    call her_main("Certainly.", "base", "base", "base", "mid", xpos="right", ypos="base", flip=False)
    m "Now, spill the beans."
    call her_main("I..I don't have any beans on me sir.", "soft", "slit", "low", "stare")
    m "(Is this girl for real?)"
    m "It's just an expression, tell me... did you complete your assignment?"
    call her_main("I did sir. I snuck into the boys dormitory using the cloak as you suggested.", "soft", "happyCl", "base", "mid")
    m "Naked?"
    call her_main("Naked... -ish", "disgust", "base", "base", "R")
    m "How can you be naked... -ish?"
    call her_main("Well, I had my underwear on, I'd be cold otherwise", "base", "base", "base", "mid")
    m "Cold? You'd have the cloak on you..."
    m "What happened next then?"
    call her_main("Well, a few of the boys were in there.", "base", "base", "base", "mid")
    call her_main("They were playing wizards chess...", "base", "base", "base", "mid")
    call her_main("Pretty poorly in fact.", "disgust", "wink", "base", "mid")

    m "..."
    m "I'm sorry miss Granger but you're going to have to do better than this."
    m "I expect better from you by now."
    call her_main("So, no points then?", "angry", "narrow", "annoyed", "mid")
    m "No, I know you can do better."
    call her_main("Fine! I'll do better next time. Double points! I'll show you!", "angry", "narrow", "angry", "R")
    m "That's the spirit. Your house will thank you when you beat the Slytherins by the end of the year."
    call her_main("Thank you professor... I'll remember that for next time.", "grin", "happy", "base", "mid_soft")

    show screen blkfade
    with d3

    show screen quistion_pop_up("{color=#cbcbcb}Hermione will remember that{/color}")
    nar "Hermione returns the next morning, looking nervous but more determined than yesterday."
    $ daytime = True
    call update_interface_color
    call music_block

    hide screen quistion_pop_up
    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d3

    call her_main("I see that you have the cloak ready for me sir.", "base", "base", "base", "R",xpos="right",ypos="base")
    m "Indeed, I'm expecting better from you today girl."
    call her_main("I won't disappoint you sir!", "grin", "base", "base", "mid")
    m "I'll be the judge of that..."

    hide screen hermione_main
    show screen day_to_night
    with d3

    $ daytime = False
    call update_interface_color
    call music_block

    nar "Later that evening a distraught-looking Hermione enters the office. "

    call her_chibi("top_naked","desk","base")
    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")

    hide screen day_to_night
    with d3

    call her_main("...", "upset", "base", "base", "mid", tears="mascara_soft",xpos="right",ypos="base")
    m "What happened? Where's your shirt?"
    call her_main("What does it look like?", "upset", "base", "base", "mid", tears="mascara_soft")
    m "Well, I know what it looks like..."
    call her_main("I didn't want to disappoint, sir, so I did what you asked...", "soft", "base", "base", "mid", tears="mascara_soft")
    call her_main("I went into the girls changing room at the quidditch pitch and put my clothes in one of the lockers.", "base", "base", "base", "mid", tears="mascara_soft")
    m "Well done. And then?"
    call her_main("I took the cloak and snuck into the boys changing room...", "base", "base", "base", "mid", tears="mascara")
    call her_main("I stood next to the doorway so that they wouldn't bump into me.", "base", "base", "base", "mid", tears="mascara")
    m "Great idea... and no one noticed?"
    call her_main("Well, at first... This damn cloak is too small.", "angry", "base", "base", "mid", tears="mascara")
    call her_main("I thought I would be short enough to fit under it...", "base", "base", "base", "mid", tears="mascara")
    call her_main("I didn't notice that my feet were visible...", "upset", "base", "angry", "mid", tears="mascara")
    m "\"Well, that's a shame.\""
    call her_main("One of the boys saw me shuffle and moved to see what it was so I tried to get away but I slipped... and... and.", "upset", "wide", "base", "shocked", tears="mascara")
    g11 "And what?"
    call her_main("And I slipped and my butt fell out!", "scream", "wide", "worried", "stare", tears="mascara")

    g9 "{size=18}Thirty points to....{/size}"

    call her_main("I'm not done!", "open", "narrow", "worried", "down", tears="mascara")
    m "Sorry, you carry on my dear!"
    call her_main("I ran out and grabbed what I could of my clothes... I think the boy may have seen me.", "soft", "narrow", "worried", "mid_soft", tears="mascara")
    call her_main("Professor.... I'm beginning to have second thoughts about this cloak idea.", "soft", "narrow", "worried", "mid_soft", tears="mascara")
    m "The boy didn't see your face, that's what matters."
    m "You could've draped the cloak around your head and it would be enough."
    call her_main("Professor!", "shock", "wide", "base", "mid", tears="mascara")
    m "Just trying to lighten the mood."
    m "Here's an extra five points for a job well done, miss Granger."
    g9 "Thirty-five points to Gryffindor!"
    call her_main("Thank you professor...", "grin", "base", "base", "mid", tears="mascara")

    call her_walk ("door", "base")

    call her_main("\"He's right, they wouldn't recognise me if I didn't show my face...\"", "base", "base", "base", "mid", cheeks="blush", tears="mascara", ypos="head", flip=False)
    call her_main("\"would they?\"", "base", "base", "base", "mid", cheeks="blush", tears="mascara")

    call her_chibi("leave")

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}End of part one.{/color}{/size}"

    $ daytime = temp_day
    $ hermione.equip(her_outfit_last)
    call update_interface_color
    call hide_screens

    jump enter_room_of_req

label a_bad_time_to_disrobe_part_2:

    call her_chibi("stand","desk","base")

    hide screen blkfade
    with d5

    call music_block
    call bld
    m "Good afternoon miss Granger."
    call her_main("Good afternoon professor, what can I do for you today?", "base", "base", "base", "mid",xpos="right",ypos="base")
    m "Glad you asked, I've got another task for you."
    call her_main("And what task may that be professor.", "soft", "base", "base", "R")
    m "Well miss Granger, I think somebody owes me a invisibility cloak."
    call her_main("Oh, do you want me to collect it from somebody?", "open", "base", "base", "mid")
    m "That somebody is you miss Granger..."
    m "You left my cloak at the scene of the crime."
    call her_main("What crime professor, what have you gotten me into?", "upset", "narrow", "annoyed", "mid")
    m "I'm talking about when you went to visit the boys changing room."
    m "Or have you forgotten already?"
    call her_main("{size=-7}I've tried to.{/size}", "upset", "base", "worried", "R")
    m "Sorry?"
    call her_main("I said, I do remember.", "normal", "base", "base", "R")
    m "Right, well. Good invisibility cloaks are pretty hard to come by..."
    m "(I think...)"
    call her_main("No they're not... they're mass produced as far as I know.", "annoyed", "base", "base", "mid")
    call her_main("By house elves I bet...", "disgust", "closed", "angry", "mid")
    m "Hey now, I know they might be small but I wouldn't call them elves."
    m "In any case, the cloak has more of a sentimental value to me... lots of memories."
    g9 "(Like the time where your butt fell out of it.)"
    g9 "Oh, the memories... you must retrieve it for me."
    call her_main("Fine, I'll do it... even though I hold you partly responsible for the situation that lead to me dropping it.", "annoyed", "closed", "angry", "mid")
    m "Great, let's not dwell on the past then."
    call her_main("...", "normal", "narrow", "annoyed", "mid")
    call her_main("Do you happen to have any idea of where it is?", "open", "base", "base", "mid")
    m "Well, it hasn't been reported as found so unless someone stole it there's only one place it could be."
    call her_main("The boys changing room?", "base", "narrow", "worried", "down")
    g9 "The boys changing room."
    call her_main("And how many house points?", "base", "base", "base", "mid")
    m "For what exactly?"
    call her_main("Retrieving the cloak of course.", "annoyed", "base", "base", "mid")
    m "You're demanding house points, for your own mistakes miss Granger?"
    call her_main("But I thought...", "upset", "base", "worried", "mid")
    m "..."
    call her_main("...", "upset", "narrow", "worried", "down")
    m "Fine, but only if we continue where we left of."
    call her_main("With my butt out?!?", "disgust", "wide", "worried", "stare")
    m "With your bu..."
    m "No, well... yes, but this time you'll be prepared."
    call her_main("But... what if they recognise me sir?", "open", "base", "worried", "mid")
    m "You'd already know if they had recognised you..."
    call her_main("(That's true...)", "soft", "base", "base", "mid_soft", cheeks="blush")
    call her_main("And then what, you want me to just walk away?", "base", "base", "base", "mid", cheeks="blush")
    m "You can figure it out yourself miss Granger. Once you have the cloak it shouldn't be an issue getting away."
    call her_main("And I want...", "open", "base", "base", "mid")
    m "I'll give you forty house points for it."
    call her_main("(I was going to ask for thirty.)", "soft", "happy", "base", "R", cheeks="blush")
    call her_main("I'll do it...", "base", "base", "base", "mid")
    g9 "Great, you're doing a great service to your house and making an old man very happy."
    call her_main("By getting your cloak back right?", "base", "base", "worried", "mid")
    m "Right..."

    call her_walk(action="leave")

    show screen day_to_night
    with d3

    $ daytime = False
    call update_interface_color
    call music_block

    nar "Later that evening"

    call her_chibi("stand","door","base")

    hide screen day_to_night
    with d3

    call her_walk("desk", "base")
    pause.5

    call her_main("...", "normal", "narrow", "base", "dead", cheeks="blush",xpos="right",ypos="base")
    m "Mission success?"
    call her_main("...", "normal", "narrow", "base", "dead", cheeks="blush")
    m "Miss Granger?"
    call her_main("Oh, hello professor, yes. Here's your cloak back.", "base", "narrow", "worried", "down")
    m "..."
    m "And?"
    call her_main("And what?", "normal", "happyCl", "worried", "mid")
    m "And what about your assignment. How did it go?"
    call her_main("Oh... yes, it went very well thank you... no hurdles in any way.", "soft", "base", "worried", "R", cheeks="blush")
    m "Your face is glowing miss Granger, I can tell when you're being untruthful."
    call her_main("It is? I didn't even notice...", "normal", "narrow", "base", "down", cheeks="blush")
    m "You're going to have to elaborate if you'd like those house points."
    call her_main("Oh... okay, I'l just go ahead then...", "mad", "base", "base", "mid")
    m "Let me get the popcorn."
    call her_main("popcorn? Where would you get popcorn from in this office?", "annoyed", "base", "base", "mid")
    g9 "Magic cupboard."
    call her_main("Right... well, I'll just start in that case shall I?", "base", "narrow", "base", "R_soft")
    call her_main("...", "base", "base", "base", "mid", cheeks="blush")
    call her_main("So... I went to the boys changing room when they were in quidditch practice.", "open", "narrow", "worried", "down")
    m "*CRUNCH*"
    call her_main("It's very messy in there... I thought the girls changing room was bad...", "base", "narrow", "base", "down")
    m "*CRUNCH* *Chew* *Chew*"
    m "*CRUNCH*"
    call her_main("Anyway... so I rummaged around in that mess...", "annoyed", "base", "worried", "mid")
    call her_main("I knew it had to have been somewhere between the showers and the doorway...", "base", "base", "base", "mid")
    call her_main("After looking around for a while I noticed that the cloak had been pushed under one of the benches lining the wall.", "open", "narrow", "worried", "down")
    call her_main("So I grabbed it and I thought I might as well disrobe and hide in the shower room with the cloak on.", "base", "narrow", "base", "down")
    call her_main("But as I was stuffing my clothes in one of the lockers a boy walked in.", "clench", "base", "worried", "mid")
    m "*CRUNCH*"
    call her_main("Professor!", "scream", "base", "angry", "mid")
    g4 "*Cough* *Cough*... sorry."
    call her_main("It is hard to talk about this as it is without your chewing distracting me.", "annoyed", "base", "angry", "mid")
    call her_main("Anyhow...", "base", "narrow", "angry", "R")
    call her_main("I expected the team to be going for at least another thirty minutes.", "open", "base", "base", "mid")
    call her_main("But that's when the boy walked in...", "normal", "closed", "base", "mid")
    call her_main("And I panicked and threw the cloak over myself and hid in one of the toilets.", "open", "base", "worried", "R")
    m "Smart."
    call her_main("...", "base", "base", "base", "mid", cheeks="blush")
    call her_main("Well, it would've been if I had remembered to lock it.", "base", "narrow", "base", "down")
    g9 "Not that smart..."
    call her_main("Do you want me to continue or not?", "annoyed", "narrow", "annoyed", "mid")
    m "You're the one receiving the points here, I'm just providing the means of earning them."
    call her_main("...", "normal", "narrow", "worried", "down")
    call her_main("As I was saying...", "base", "narrow", "base", "down")
    call her_main("I went into one of the toilets and I heard the boy shuffling outside.", "base", "closed", "base", "mid")
    call her_main("The room was so small so I tried to back into a corner, but as he came in I knew it wasn't going to work...", "base", "narrow", "base", "down", cheeks="blush")
    call her_main("So I prayed he wasn't about to sit down and instead I positioned myself above the toilet with my legs around the base.", "clench", "happyCl", "worried", "mid")
    m "And did he sit down or not?"
    call her_main("No, but he was close enough for me to feel his...", "mad", "squint", "worried", "up")
    call her_main("His...", "base", "slit", "worried", "ahegao")
    m "His what? miss Granger..."
    call her_main("Well... His Penis brushed up against my butt.", "annoyed", "closed", "base", "mid", cheeks="blush")
    m "How did he manage that?"
    call her_main("The boy wasn't in there to relieve himself in the way I assumed...", "open", "closed", "angry", "mid", cheeks="blush")
    call her_main("I guess he wasn't paying attention to what sensation he was feeling on the tip of his...", "normal", "base", "worried", "mid", cheeks="blush")
    call her_main("Anyway...", "open", "base", "worried", "R", cheeks="blush")
    m "..."
    call her_main("I'd like my points now.", "base", "narrow", "worried", "down")
    m "Certainly miss Granger..."
    m "Forty points to Gryffindor!"
    call her_main("Thank you professor...", "soft", "base", "base", "mid_soft")

    call her_walk("door", "base")

    call her_main("(I'm glad I had time to clean the cloak before walking in here...)", "base", "narrow", "base", "dead", cheeks="blush", flip=True)
    call her_main("(That thing was massive...)", "normal", "narrow", "worried", "down", cheeks="blush")
    call her_main("(What am I thinking? snap out of it...)", "base", "happyCl", "worried", "mid", cheeks="blush")

    call her_chibi("leave")

    call blkfade
    centered "{size=+10}{color=#cbcbcb}The end{/color}{/size}"

    call hide_screens
    $ daytime = temp_day
    call update_interface_color

    $ hermione.equip(her_outfit_last)

    jump enter_room_of_req
