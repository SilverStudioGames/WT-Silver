

### Tonks Hangout Event ###

label tonks_hangout:

    call setup_fireplace_hangout(char="tonks")##

    $ tonks.strip("robe") # Takes off robe

    $ nt_he_counter += 1
    if firewhisky_ITEM.owned >= 1:
        $ firewhisky_ITEM.owned -= 1

    $ nt_he_drink.start()

    label tonks_hangout_continue:
        hide screen bld1
        with fade
        call bld

    ### Intro Events ###

    # Hermione
    if hermione_intro.E5_complete and not nt_he.hermione_E1:
        jump nt_he_hermione_E1 # Persuade Hermione to sell favors.

    # Susan
    if her_tier >= 2 and ton_friendship >= 20 and not nt_he.susan_E1:
        $ ag_event_pause += 2 # Astoria intro happens in 2 days.
        jump nt_he_susan_E1 # Starts Susan/Astoria intro.

    # Astoria
    if astoria_intro.E3_complete and not nt_he.astoria_E1:
        jump nt_he_astoria_E1

    # (Quidditch) Ask Tonks for help with Slytherins.
    if cho_quid.E6_complete and not cho_quid.E8_complete:
        jump cho_quid_E8

    ### General Events ###

    if her_tier >= 2 and not nt_he.favors_E1:
        jump nt_he_favors_E1 # Unlocks Public Requests.
    if ton_reputation >= 4 and ton_friendship >= 20 and not nt_he.favors_E2:
        jump nt_he_favors_E2 # Tonks Tier 2 available.


    ### Snape Stories ###

    if ton_support < 12:
        $ random_number = 1
    else:
        $ random_number = renpy.random.randint(1, 3)

    if random_number == 1:
        if ton_support < 12:
            $ ton_support += 1
        $ nt_he_story.start()

    label end_tonks_hangout:

    $ d_flag_01 = "afternoon" if game.daytime else "evening"

    if ton_friendship < 100:
        call notes
        ">You spend the [d_flag_01] hanging out with Tonks.\n>Your relationship with her has improved."
    else:
        ">You spend the [d_flag_01] hanging out with Tonks."

    label end_tonks_hangout_points:

    if ton_friendship < 100: # max
        if fire_in_fireplace: # Tonks is feeling hot.
            $ ton_friendship += 2

        if game.difficulty < 2:      #Easy difficulty
            $ ton_friendship += 5
        elif game.difficulty == 2:   #Normal
            $ ton_friendship += 4
        else:                        #Hardcore
            $ ton_friendship += 3

    if ton_friendship > 100:
        $ ton_friendship = 100

    $ tonks.wear("all")
    $ chair_OBJ.hidden = False

    if game.daytime:
        jump night_start
    else:
        jump day_start



label nt_he_wine_intro:
    call bld
    m "Care for a drink?"
    call ton_main("Of course, [ton_genie_name].", "base", "base", "shocked", "mid", cheeks="blush", ypos="head", flip=False)
    call ton_main("Hit me!","horny","base","base","down")
    pause.1

    # Show wine
    call give_gift(">You hand over the bottle you found in the cupboard to professor Tonks...", wine_ITEM)

    call ton_main("Wine?","open","base","raised","down")
    call ton_main("Don't you have anything stronger?","upset","base","base","R")
    m "Like what?"
    call ton_main("How about firewhisky? Got any of that?","open","base","base","mid")
    m "I'm afraid not..."
    call ton_main("What a bummer. I guess wine will do for today.", "upset", "base", "worried", "down")
    m "(Maybe there is some of that other stuff stored in the cupboard as well...)"

    # Make firewhisky available in the cupboard and store
    $ firewhisky_ITEM.unlocked = True

    jump tonks_hangout_continue


label nt_he_firewhisky_intro:
    call bld
    g9 "Look what I've got!"
    pause.1

    # Show firewhisky
    call give_reward(">You hand over a bottle of firewhisky to Tonks...", gift="interface/icons/item_whisky.webp", sound=False)

    call ton_main("Finally, the good stuff!","horny","base","base","down", ypos="head", flip=False)
    call ton_main("I'm glad you brought out some firewhisky this time...","base","base","base","down")
    call ton_main("Wine makes me giggly, and hinders my judgment.", "base", "base", "base", "L")
    m "..."
    call ton_main("Got a frog in your throat?","open","base","raised","mid")
    m "No, I was just waiting for an opening."
    call ton_main("Sorry, I guess I talk a lot once I get going...", "mad", "base", "shocked", "R")
    call ton_main("Bottoms up.","horny","base","base","down")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.6}{nw}", "base", "closed", "worried", "mid", trans=hpunch)
    call ton_main("*Cough* *Cough*", "open", "happyCl", "shocked", "stare")
    call ton_main("Yeah, that was a mistake.", "mad", "base", "base", "down")
    m "I don't drink whisky that often, but even I know not to down it in one..."
    call ton_main("*Mmm*... that's the stuff.", "horny", "narrow", "base", "down")
    m "Are you even listening?"

    jump tonks_hangout_continue


label nt_he_firewhisky_E1:
    call bld
    m "Another glass of firewhisky?"
    call ton_main("Fill 'er up.", "horny", "base", "base", "up", ypos="head", flip=False)
    call ton_main("...", "base", "base", "shocked", "down")
    call ton_main("A little bit more...","open","base","raised","down")
    call ton_main("A bit more...","horny","base","angry","down")
    call ton_main("That's it, cheers.", "base", "base", "base", "mid")

    if nt_he_drink.counter <= 3: # First time only.
        if game.daytime:
            m "Boring lessons ahead?"
            call ton_main("Not particularly, why?","open","base","base","mid")
            m "You might regret going back to classes after drinking this much."
            call ton_main("Oh don't you worry, [ton_genie_name].", "silly", "happyCl", "base", "mid")
            call ton_main("I could down this entire bottle without anybody being able to notice a thing.","horny","base","base","L")
            m "You're one glass in and swaying like a buoy..."
            call ton_main("*Hic* Oh well...","open","base","base","ahegao", trans=hpunch)
            call ton_main("No risk, no fun!","horny","base","base","mid")
        else:
            m "Long day?"
            call ton_main("Not in particular, why?", "open", "wide", "raised", "mid")
            m "..."
            m "No reason..."

    jump tonks_hangout_continue


label nt_he_firewhisky_E2:
    call bld
    m "More firewhisky?"
    call ton_main("Thought you'd never ask...","horny","base","base","down", ypos="head", flip=False)

    jump tonks_hangout_continue


label nt_he_firewhisky_E3:
    call bld
    m "Want to get drunk?"

    call ton_main("Of course.", "base", "narrow", "shocked", "down", ypos="head", flip=False)
    if game.daytime:
        call ton_main("I'm not going to regret this, am I?", "clench", "base", "raised", "downR")
        call ton_main("Hopefully my students won't notice...", "grin", "narrow", "base", "downR")
    else:
        call ton_main("I'd never say no to that!","horny","base","base","down")

    jump tonks_hangout_continue


label nt_he_firewhisky_E4:
    call ton_main("Bottoms up.", "base", "narrow", "base", "mid", ypos="head", flip=False)
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}","scream","closed","base","mid")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}","scream","closed","worried","mid")
    call play_sound("gulp")
    call ton_main("*Gulp*{w=0.8}{nw}", "scream", "closed", "worried", "mid")
    call ton_main("*Aaaaaaaahhhh!!!*...", "silly", "closed", "base", "ahegao", trans=vpunch_repeat)
    m "....................."

    jump tonks_hangout_continue



### Events ###

label nt_he_favors_E1:
    call ton_main("So, [ton_genie_name]... what's the going rate around here then?", "open", "base", "raised", "mid", ypos="head", flip=False)
    m "Going rate?"
    call ton_main("How much do you pay your students to fool around?", "base", "narrow", "annoyed", "mid")
    m "Oh... It depends on what you want them to do."
    call ton_main("How much for a lap dance?", "soft", "narrow", "raised", "mid")
    m "Again, it depends on the student."
    call ton_main("...","upset","base","base","R")
    m "But if I had to guess, I'd say about twenty-five points."
    call ton_main("Unbelievable that you've managed to convince these girls to offer themselves up to you, for a bunch of imaginary points...", "base", "narrow", "annoyed", "R")
    m "Works for the internet..."
    call ton_main("The what?","open","base","raised","mid")
    m "A place you go when you want to procrastinate..."
    m "Or you happen to be sitting on the toilet..."
    m "Anyway, you can't just ask for a lap dance straight away, You have to butter them up first."
    call ton_main("How so?", "mad", "base", "raised", "mid")
    m "Well most of them aren't going to do whatever you say from the get go..."
    m "You have to slowly earn their trust over time and start out small..."
    call ton_main("*Awww*... really? Can't I just cheat a bit?","upset","base","worried","L")
    m "..."
    m "Just take it slow, I'm sure you'll find a cute boy who'll be willing to do whatever you want anyway."
    call ton_main("...","upset","base","base","R")
    call ton_main("But what if I want a girl?","horny","base","raised","mid")
    g4 "(...!)"
    m "Whatever floats your boat."

    $ tonks_requests_unlocked = True
    call popup("You can now ask Tonks to do \"Public Requests\" with her students!", "Congratulations!", "interface/icons/head/tonks.webp")

    $ nt_he.favors_E1 = True

    jump end_tonks_hangout_points


label nt_he_favors_E2:
    call ton_main("You know, [ton_genie_name]... I overheard a couple of students whispering about me...", "open", "base", "raised", "mid", ypos="head", flip=False)
    g9 "Finally..."
    call ton_main("I walked past a group of boys the other day...","open","base","base","R")
    call ton_main("One straight up called me a slut, whilst the others snickered at me...","open","base","base","down")
    m "Oh?"
    call ton_main("So, I turned around and told him that such behaviour could earn him detention...", "base", "wink", "base", "mid")
    call ton_main("Of course, word has it that detention with me is rather enjoyable...","horny","base","base","mid")
    call ton_main("And I believe that group of boys knew that fact as well...", "base", "base", "angry", "R")
    m "Sounds like it's about time we step it up a notch."
    call ton_main("And behave even riskier?", "open", "shocked", "shocked", "mid")
    call ton_main("Who do you think you're asking exactly?","open","closed","base","mid")
    m "So...{w=0.3} Is that a yes?"
    call ton_main("Fuck yes!", "grin", "narrow", "shocked", "mid")
    call ton_main("I want those boys to call me all sorts of names... And do it straight to my face!","horny","base","angry","mid")
    g9 "Promise me you'll reward them if they do."
    call ton_main("I promise, [ton_genie_name].", "base", "wink", "base", "mid")

    call popup("Tonks can now reach the next level!", "Congratulations!", "interface/icons/head/tonks.webp", sound=False)

    $ nt_he.favors_E2 = True

    jump end_tonks_hangout_points



### Tonks Auror Stories ###

label nt_he_story_intro_E1:
    call ton_main("Thanks for accepting my job application by the way.","base","base","base","mid", ypos="head", flip=False)
    m "I didn't really have that much choice in the matter."
    call ton_main("Oh, yeah...", "grin", "narrow", "base", "downR")
    call ton_main("...", "annoyed", "base", "base", "R")
    call ton_main("I'll do well...{w=0.4} you'll see.", "open", "base", "base", "down")
    call ton_main("After all, I was taught by one of the best aurors there is.", "base", "base", "raised", "mid")
    call ton_main("So, don't get me wrong... I do wish to teach those students a couple of useful things while I'm here...", "annoyed", "base", "shocked", "mid")
    call ton_main("Teaching a class of beginners should be a breeze.", "base", "narrow", "base", "mid")
    m "I never said I doubted your abilities."
    call ton_main("Maybe I'll give you a demonstration some day...", "horny", "base", "raised", "mid")
    call ton_main("And I'm not talking about my intellectual abilities...", "horny", "base", "base", "down")
    g9 "I'm a well for all kinds of knowledge!"

    if game.daytime:
        call ton_main("Anyway, I have to go prepare for classes.","open","base","base","R")
    else:
        call ton_main("Anyway, I think I'm gonna go hit the sack.","open","base","base","R")

    if nt_he_drink.is_event_complete(1, 2): # We're past the wine intro
        m "There's more firewhisky where this came from, so feel free to stop by any time to talk about your progress."
        call ton_main("I'll never say no to a free drink.","base","base","base","down")
    else:
        m "There's more wine where this came from, so feel free to stop by any time to talk about your progress."
        call ton_main("Please, no more wine! You better have some firewhisky next time.","open","base","worried","mid")
        m "Oh, right. I'll make sure to get some."
        call ton_main("Good!","base","base","base","mid")

    call ton_main("And I'll keep you updated on the academics as usual.","base","base","base","mid")
    m "(That's not the kind of progress I meant...)"

    jump end_tonks_hangout


label nt_he_story_intro_E2:
    call bld
    m "You mentioned an auror last time if I'm not mistaken."
    call ton_main("Moody?", "annoyed", "wide", "shocked", "mid", ypos="head", flip=False)
    m "Not in particular."
    call ton_main("What?", "mad", "base", "raised", "mid")
    m "..."
    call ton_main("You talking about Mad-eye?", "upset", "base", "raised", "mid")
    m "I can see perfectly fine, dear."
    call ton_main("Alastor Moody is the auror that taught me.", "open", "narrow", "annoyed", "mid")
    m "Oh, of course."
    m "(His parents must have hated him...)"
    #m "(What's wrong with a normal name... like Will Smith, or Robin Williams?)"
    m "Anything you'd like to tell me about him?"
    call ton_main("Well, he's a bit of a weirdo, but he knows his stuff.", "open", "closed", "annoyed", "mid")
    call ton_main("I guess if you're as paranoid as him, you'll end up knowing everything there is about the craft...", "open", "base", "base", "R")
    m "Paranoid of what?"
    call ton_main("Dark wizards.", "mad", "narrow", "base", "mid")
    m "So...{w=0.3} He's a racist?"
    call ton_main("No, but he's old... I think he should just retire to be honest.", "open", "base", "base", "downR")
    call ton_main("His methods have gotten progressively more nefarious...", "open", "narrow", "annoyed", "R")
    call ton_main("Some would argue he should be locked up himself, for all the things that he did to catch his targets...", "mad", "narrow", "base", "down")
    g9 "And you?"
    call ton_main("Me? What about me?", "upset", "narrow", "annoyed", "mid")
    m "You wouldn't say what we do is unethical as well?"
    call ton_main("Did you start drinking before I got here?", "open", "narrow", "annoyed", "L")
    m "I never stop..."
    call ton_main("...", "annoyed", "closed", "base", "up")

    jump end_tonks_hangout


label nt_he_story_intro_E3:
    call ton_main("Do you always happen to have a bottle ready for me?", "base", "base", "raised", "down")
    g9 "For you, always."
    call ton_main("I don't even have to visit the Hog's Head to get a drink anymore...", "base", "narrow", "annoyed", "R")
    m "Why go anywhere when you've got a magic cupboard that fills itself with alcohol."
    call ton_main("It does?", "open", "wide", "raised", "mid")
    m "At least I think that's how it works..."
    m "I may be a Genie, but I can't just turn water into wine... or whisky."
    m "(At least not in this world...)"
    call ton_main("Yeah, that would be impressive.", "silly", "happyCl", "base", "mid")
    call ton_main("I haven't found a single wizard that could do that.", "open", "closed", "shocked", "mid")
    m "Ah yes. Because all those cunning bachelors are already taken...{w} or gay..."
    call ton_main("No. Single as in... no one can do it.", "open", "narrow", "base", "mid")
    call ton_main("It's almost impossible to summon drinks and food out of thin air.", "open", "base", "base", "R")
    call ton_main("Best they can do is conjure water out of the surrounding humidity.","upset","base","base","R")
    m "If only I had my powers... I could do it with a snap of a finger."
    call ton_main("I'm sure you could...", "silly", "happyCl", "base", "mid")

    ">You brag about your almighty powers in front of the witch..."
    ">If only you hadn't lost them..."

    #m "(What kind of shit wizard can't even make food...)"
    #m "What about water though, doesn't that count as a drink?"
    #call ton_main("...","base","base","base","mid")
    #call ton_main("You know what, I never thought of that.","base","base","base","mid")
    #m "What even counts as food or drink... sound pretty arbitrary to me."
    #call ton_main("I don't think we're supposed to think about it too hard.","base","base","base","mid")
    #m "Less obvious plot-holes that way I suppose..."
    #call ton_main("Less what, sorry?","base","base","base","mid")
    #m "No matter, just thinking out loud is all."

    jump end_tonks_hangout


label nt_he_story_intro_E4:
    call ton_main("I've been so busy lately... The days here fly by faster than a Firebolt.", "open", "closed", "worried", "mid", ypos="head", flip=False)
    m "I'm not sure I know that... spell?"
    call ton_main("It's a broom...", "upset", "base", "base", "mid")
    m "Oh, I see... I'm not really that into brooms."
    m "Or anything that is inconveniently stiff and long to ride on..."
    call ton_main("Well I don't mind that... Most witches don't.", "grin", "base", "base", "R")
    g9 "You should ask me about my knowledge of flying carpets instead!"
    g9 "I can tell you everything about the newest model."
    call ton_main("Do you own one yourself? A flying carpet?", "silly", "base", "base", "mid")
    m "No... But a friend of mine does."
    m "It's more of a pet, actually."
    m "Technically they are sentient beings..."
    call ton_main("Yes, I've heard of that... How interesting.", "silly", "happyCl", "base", "mid")
    call ton_main("So...{w=0.4} Would you like that? Own a pet, that is...","base","base","angry","mid")
    m "Sure. Why do you ask?"
    call ton_main("Just out of curiosity...","horny","base","base","mid")
    m "(...)"

    ">You keep thinking about what Tonks meant by that, whilst she eyes you up expectantly..."

    jump end_tonks_hangout


label nt_he_story_intro_E5:
    call bld
    m "You still haven't told me anything about your time as an auror..."
    call ton_main("Well, what would you like to know?", "open", "wide", "raised", "mid", ypos="head", flip=False)
    m "That \"moody\" guy taught you, you said. You could start there."
    call ton_main("Well, the job of an auror is a bit different now than how it was ten or so years ago.", "open", "base", "base", "R")
    call ton_main("I studied to become an auror with the hopes of taking down evil wizards.", "annoyed", "base", "annoyed", "down")
    m "Sounds like a nineties B movie to me."
    call ton_main("A what?", "normal", "shocked", "raised", "mid")
    m "Never mind... continue."
    call ton_main("In any case... That's not at all how the job is anymore.", "mad", "base", "base", "R")
    m "Was it ever?"
    call ton_main("That's what they told me...", "annoyed", "base", "annoyed", "R") #'tell' to 'told'
    call ton_main("But right now, it's mostly droves of paperwork.", "open", "closed", "annoyed", "mid")
    call ton_main("Back in the day, they never used to bother with it.", "upset", "base", "base", "mid")
    m "Don't you have people for that sort of thing?"
    call ton_main("We're our own division, and are supposed to follow strict guidelines set by the ministry.", "open", "closed", "base", "mid")
    call ton_main("There was too much bad stuff happening for anyone to lecture the aurors though...", "normal", "base", "annoyed", "R")
    m "Then why did you stay?"
    call ton_main("I'm here, aren't I?", "upset", "base", "raised", "mid")
    call ton_main("Why do you think I jumped on the opportunity to teach here?","open","base","base","mid")
    m "(You kind of created that opportunity yourself...)"
    call ton_main("I learned a lot, though, and I always wanted to use that knowledge to teach others...", "base", "narrow", "base", "mid")
    call ton_main("I just didn't think I was up for it yet. Not until I stepped through these halls again...","open","base","base","mid")
    call ton_main("It made me realise how much I've missed being here.", "grin", "wide", "shocked", "mid")

    jump end_tonks_hangout


label nt_he_story_E6:
    call ton_main("Did I ever tell you about the time we arrested a vampire?", "open", "wide", "base", "mid", ypos="head", flip=False)
    m "You haven't even told me about your \"defence against the dark arts\" training yet, but sure, go ahead..."
    call ton_main("Right... Well, there was this vampire guy.", "soft", "base", "base", "R")
    call ton_main("We spent ages looking for him, and found that he had been disguising himself as a headmaster of a muggle school.", "mad", "narrow", "base", "downR")
    m "..."
    call ton_main("It was quite disgusting what he was doing to the students actually...", "annoyed", "closed", "angry", "mid")
    call ton_main("He even brought over some of the teachers... They're never going to be the same...", "disgust", "closed", "angry", "R")
    m "..."
    call ton_main("Corrupted... Forever...", "soft", "closed", "angry", "mid")
    m "(Not sure if I should feel bad at this point...)"
    call ton_main("Kind of hot, though... don't you think?", "horny", "wink", "angry", "mid")
    m "(Never mind...)"
    call ton_main("The immense power vampires have over their prey...","horny","base","raised","ahegao")
    call ton_main("It's a shame that they're slaves to their own urges.","open","closed","worried","mid")
    m "(Well... there's that bad feeling I felt before.)"
    call ton_main("I get it though. Some aspects of it at least...","upset","base","base","R")

    jump end_tonks_hangout


label nt_he_story_intro_E7:
    call bld
    m "Now, I'm starting to feel like you've been avoiding the subject of your auror training."
    call ton_main("Is it that obvious?", "mad", "base", "base", "R", ypos="head", flip=False)
    m "You brought up vampires last time without even saying hello."
    call ton_main("Vampires are interesting...", "soft", "base", "worried", "downR")
    m "..."
    call ton_main("Fine, I didn't want to talk about some of Moody's teaching methods...","open","closed","base","mid")
    call ton_main("They tend to be quite... unconventional.", "clench", "base", "base", "R")
    m "Like how?"
    call ton_main("Well...", "upset", "base", "shocked", "down")
    call ton_main("Moody very much believed in learning by doing.", "open", "base", "base", "mid")
    m "Sounds reasonable enough..."
    call ton_main("This is defence against dark magic we're speaking of...","open","base","raised","mid")
    call ton_main("Some of the spells and situations he put me in are borderline -- if not completely -- illegal.","open","base","angry","mid")
    m "Surely in a controlled environment where there's no harm to both parties..."
    call ton_main("Well... That was true most of the time...", "clench", "base", "base", "R")
    call ton_main("(I can't believe I'm talking about this...)","upset","base","worried","down")
    call ton_main("(The ministry will kick Moody out faster than a Blast-ended Skrewt going off if I'm not careful...)", "mad", "base", "worried", "R")

    jump end_tonks_hangout


label nt_he_story_E8:
    call ton_main("I'll tell you about this one time where Moody went a bit too far.", "normal", "base", "base", "downR", ypos="head", flip=False)
    m "Where did this sudden urge of sharing come from?"
    call ton_main("Oh, I've been wanting to spill the beans about this for ages. I just didn't want to get anyone in trouble at the ministry...", "normal", "closed", "base", "mid")
    m "What's to say I won't get you into trouble?"
    call ton_main("You won't... Would you?", "open", "shocked", "worried", "mid")
    m "No..."
    call ton_main("Right...", "upset", "closed", "base", "mid")
    call ton_main("Anyway, he once brought in this werewolf that we had put in custody.", "mad", "base", "base", "down")
    g4 "He did what?!?"
    call ton_main("See, I knew you'd react like that.", "disgust", "narrow", "shocked", "down")
    m "No, I was just taken by surprise... I didn't know they existed."
    call ton_main("Of course they do, silly!", "soft", "narrow", "annoyed", "R")
    call ton_main("So, he brought in this werewolf... apparently quite harmless comparatively.","open","base","base","R")
    m "Compared to what? A dog?"
    call ton_main("Compared to werewolves like Fenrir Greyback...", "upset", "closed", "angry", "L")
    m "Oh yeah..."
    m "That...{w=0.4} Guy..."
    call ton_main("Moody had worked out a deal with this guy...","open","base","base","mid")
    call ton_main("To see how I would react in a real life situation where he would turn.", "annoyed", "base", "angry", "mid")
    m "Turn where?"
    call ton_main("Into a werewolf.", "clench", "closed", "angry", "mid")
    m "Of course."
    call ton_main("So, the thing is... we hadn't taken into account that it was mating season for them...", "mad", "narrow", "base", "down")
    g9 "You don't say!"
    call ton_main("The guy wasn't that interested in biting me that's for sure.", "soft", "base", "base", "downR")
    call ton_main("So you can see why I wasn't so keen on reporting it. More of an embarrassing situation sort of thing than anything else.","open","base","base","R")
    call ton_main("And it was totally our fault, I should've recognised the signs straight away... when they're turned they're largely driven by their instincts.", "open", "base", "shocked", "down")
    m "I see."
    call ton_main("Dated him for a while...","horny","base","base","R")
    g4 "You did what?"
    call ton_main("Satiated my need for a dominant male relationship for a couple of months, that's for sure...", "base", "narrow", "angry", "down")
    m "(That explains a few things...)"

    jump end_tonks_hangout


label nt_he_story_intro_E9:
    call ton_main("Being an auror was quite a stressful job you know.", "open", "closed", "shocked", "mid", ypos="head", flip=False)
    m "I--"
    call ton_main("The ministry was mostly concerned about the criminals making up for their crimes.","open","base","angry","mid")
    call ton_main("But I was more concerned about the victims involved.","open","closed","base","mid")
    call ton_main("So, sometimes there would be a situation that I'd take into my own hands.", "open", "closed", "shocked", "mid")
    m "Such as?"
    call ton_main("Well, there was this one guy that used a love potion...", "normal", "narrow", "base", "R")
    m "A love potion, too bad they aren't real..."
    call ton_main("Of course they're real, and quite effective as well.", "open", "wide", "base", "mid")
    call ton_main("Also... highly illegal.", "soft", "closed", "base", "mid")
    m "Oh, of course..."
    call ton_main("Anyway...","open","base","base","L")
    call ton_main("He could've ended up in prison... but law isn't black and white like that.","open","base","base","mid")
    m "So you're saying that his intentions were good?"
    call ton_main("In this instance, the woman in question was in an abusive relationship.", "open", "base", "base", "R")
    call ton_main("And the guy knew that the boyfriend was the jealous type...","open","base","base","mid")
    m "I see, so he fed her the potion to get her out of it."
    call ton_main("Right... I mean jealousy isn't that bad in a playful relationship. But it wasn't like that.", "normal", "base", "base", "downR")
    m "Wait a second, how did you even know the guy wasn't just saying this because the potion is illegal?"
    call ton_main("Because I used truth serum.", "grin", "base", "raised", "mid")
    m "And that isn't illegal or regulated as well?"
    call ton_main("As I said... Law is more complicated than that, and in certain instances using a truth serum would be the right thing to do.", "mad", "base", "base", "mid")
    call ton_main("And to be honest, who was he going to tell... It's not like he had the moral high ground.", "annoyed", "closed", "base", "mid")
    m "I see, then how did the situation end up?"
    call ton_main("The girl got out of the abusive relationship and requested to have her memory adjusted.", "open", "wide", "shocked", "mid")
    m "And that's--"
    call ton_main("That's fine if the person in question is okay with it.","open","base","base","R")
    call ton_main("They have to sign a form and all that...","base","base","base","mid")
    m "Obviously..."
    m "(Where do these people draw the line... making someone fall in love with you just like that?)"
    m "(...)"

    jump end_tonks_hangout


label nt_he_story_intro_E10:
    call bld
    m "Settled in okay?"
    call ton_main("Yes, I finally feel like I've found some sort of daily routine.", "grin", "wide", "base", "mid", ypos="head", flip=False)
    call ton_main("This school brings back so many memories. It's like, every time I turn a corner I expect to see one of my old classmates.", "open", "base", "shocked", "R")
    m "So, good memories?"
    call ton_main("Mostly, it's a bit different now.", "base", "narrow", "shocked", "down")
    m "In what way?"
    call ton_main("Well, there wasn't any of this favour business going on for one.", "horny", "base", "base", "R")
    call ton_main("But the students and teachers were pretty much the same.", "base", "base", "raised", "down")
    m "So, what was the real old man like?"
    call ton_main("Unobtrusive...", "open", "base", "raised", "R")
    m "What does that mean?"
    call ton_main("I only really saw him during larger festivities, he mostly spent his time in this office.", "open", "base", "base", "down")
    m "So that's why Snape wanted me to stay put..."

    jump end_tonks_hangout


label nt_he_story_E11:
    $ tonks_morph_known = True
    call bld
    m "Tell me more about your time at Hogwarts, as a student..."
    call ton_main("Of course, [ton_genie_name].","base","base","base","mid", ypos="head", flip=False)
    call ton_main("Well, as you may or may not know. I'm a metamorphmagus.","open","base","base","R") #metamorphmagus is a latin based word, therefore "-us" is the singular version and "-i" is the plural
    call ton_main("It means I can change my physical appearance at will.", "base", "base", "raised", "mid")
    m "Sounds useful."
    call ton_main("It can be.","base","base","base","L")
    call ton_main("Since you can't reprimand me about it, I might as well tell you a bit about it.","open","base","raised","mid")
    m "I'm still your boss."
    call ton_main("You gonna put me in detention?","horny","base","base","mid")
    call ton_main("Or put me over your knee and spank me?","horny","base","angry","mid")
    g9 "Don't tempt me."
    call ton_main("There was this time where I changed into professor Snape.", "grin", "narrow", "base", "mid")
    m "Why Snape?"
    call ton_main("Well, he was the most likely not to be in the staff room. Which is where I wanted to get in.", "grin", "narrow", "base", "R")
    m "Why's that?"
    call ton_main("He never leaves the dungeons does he?", "open", "wide", "raised", "mid") #pretty sure in the books they always refer to it as multiple dungeons but could be wrong
    call ton_main("Just take one look at his pasty face and you'll see...", "mad", "base", "base", "downR")
    call ton_main("Don't tell him I said that...", "clench", "base", "base", "mid")
    g9 "..." #[Smirk]
    call ton_main("So... I changed into professor Snape and went towards the staff room...", "base", "base", "annoyed", "R")
    m "Isn't the staff room just full of boring old teachers?"
    #call ton_main("Have you used a mirror lately?","open","base","raised","mid")
    call ton_main("My goal wasn't to talk with the teachers...", "open", "closed", "base", "mid")
    call ton_main("I was trying to get a key to the prefects' bathroom.", "base", "base", "angry", "mid")
    m "And you couldn't just turn into a prefect, and get in there that way?"
    call ton_main("Well, that would've been the clever thing to do...", "open", "base", "raised", "R")
    call ton_main("Although like everything else in this school, the bathroom has a password and not a key...", "normal", "closed", "annoyed", "mid")
    call ton_main("Of course I didn't know that... I had just heard rumours about the bathroom.", "clench", "narrow", "worried", "R")
    m "So did you manage to get in there in the end?"
    call ton_main("Oh yeah, it was easy!", "base", "wink", "base", "mid")
    call ton_main("Once I knew about the password I just had to pretend to be one of the prefects, and ask another for it.", "open", "wide", "base", "mid")
    m "Smart..."

    jump end_tonks_hangout


label nt_he_story_E12:
    call bld
    m "Tell me more about that shapeshifting ability of yours..."
    call ton_main("Of course...", "base", "wide", "shocked", "mid", ypos="head", flip=False)
    call ton_main("Most of my escapades were kind of one trick ponies.", "open", "base", "base", "R")
    m "Sounds pretty foolproof to me..."
    m "I mean how many other students could change their appearance?"
    call ton_main("None, that's why. Process of elimination.", "upset", "base", "raised", "downR")
    m "So you got punished without any sort of proof?"
    call ton_main("No, but they set up countermeasures after the time when...", "open", "base", "raised", "R")
    call ton_main("I shouldn't really talk about it. They never confronted me about it so fessing up now isn't going to do me any good.", "mad", "narrow", "worried", "down")
    m "Not a word leaves this office."
    call ton_main("Do you think I'm weird?", "open", "narrow", "shocked", "down")
    m "Everyone is a bit... weird..."
    call ton_main("Fine, I'll tell you.", "base", "closed", "shocked", "down")
    call ton_main("You might have noticed but I'm a bit more comfortable with my sexuality than most people.","open","base","base","mid")
    g9 "(Oh, here we go!)"
    call ton_main("I already told you about the whole werewolf thing, and the power play fantasies with the vampire...","open","base","base","R")
    m "Well, you didn't phrase it that bluntly before but I got the gist."
    call ton_main("Well, just like many weird or odd sexual preferences they're often deeply embedded with experiences from your youth.","open","base","worried","L")
    call ton_main("So for me, there was this one time where I pretended to be a teacher...","open","base","worried","mid")
    call ton_main("As in, I literally took over their lesson when they were ill.", "mad", "base", "base", "down")
    m "How did you manage that, weren't the students notified of their leave beforehand?"
    call ton_main("No. There was just a note on the door, so I ripped it off before the class got there.","open","closed","base","mid")
    m "Seems like a flawed system..."
    call ton_main("Yeah, afterwards a lot of the teachers changed the way they do it. Not the new ones though...", "grin", "base", "base", "downR")
    m "You haven't told me which class this was. Did you turn into Snape and teach potions?"
    call ton_main("Of course not! Snape would've made my life hell, and I wasn't going to make someone hurt themself. ", "open", "base", "annoyed", "down")
    call ton_main("It was charms...", "mad", "base", "base", "down")
    m "Right..."
    call ton_main("I had been practising some charms, and taught myself a couple on my own, like the one for invisibility...", "crooked_smile", "base", "base", "down")
    m "Impressive."
    call ton_main("Thanks... Normally you wouldn't learn that one until much later, so you'd easily be able to dispel it.", "silly", "happyCl", "base", "mid")
    m "But you decided it was a good idea to teach it anyway?"
    call ton_main("I didn't say it was a good idea.", "mad", "base", "base", "mid")
    call ton_main("It didn't end up working anyway...","upset","base","worried","R")
    call ton_main("Instead of the charm making the students' whole body transparent, it just made their clothes vanish!", "open", "closed", "base", "mid")
    call ton_main("Whilst it wasn't intentional, the memory of it still excites me a bit.","base","base","base","down")
    call ton_main("And that's where that particular fetish came from...", "soft", "base", "base", "mid")
    g4 "Hold on, there's a spell to make only the clothes invisible?"
    call ton_main("That's what you focus on?","open","base","raised","mid")
    m "Well, yeah! Sound to me like you invented a new spell that no one's ever heard of..."
    g4 "And it can make people's clothing invisible?! That's kind of a big deal!"
    call ton_main("It's not a new spell... it was just novice wizards and witches not being powerful enough to cast it properly...", "upset", "wide", "shocked", "mid")
    call ton_main("Similarly to splinching.", "clench", "base", "raised", "R")
    m "(That sounds disgusting...)"
    call ton_main("Anyway, the teachers played it off as an accident... though poor Flitwick had his magical abilities questioned by the students for a while.", "upset", "base", "shocked", "down")
    call ton_main("And they tried to set up some more countermeasures towards my abilities at that point.", "open", "base", "annoyed", "R")
    call ton_main("Not that they worked that well... After that I was a bit more selective with my usage, and actually thought about the consequences a bit before using it.", "mad", "narrow", "annoyed", "R")
    m "Well, you do start thinking more about others as you get older..."
    call ton_main("Yeah well, my sexual drive started to take the upper hand on my decisions from that point on, so it evened out.", "base", "happyCl", "base", "mid")
    m "(...)"

    jump end_tonks_hangout



### Centaur Story ###

# Will be something other than a hangout event as you can't have a jerk-off interaction during them.
# Substitute Teacher for Care for Magical Creatures maybe?

label nt_he_story_centaur: # Not in use.
    call ton_main("...","upset","base","worried","mid")
    call ton_main("Very well, Professor.{w} I think I can make an exception for you.","open","base","base","R")
    g9 "And spare no details."
    call ton_main("I have your word that you will not tell a soul about any of this?","open","base","base","mid")
    g4 "Yes... now tell me!"

    call ton_main("Very well...","upset","base","worried","down")
    call ton_main("First you should know, there aren't many witches that could take on and calm a large group of wild centaurs...","open","base","worried","mid")
    call ton_main("Most would foolishly try to intimidate or threaten them, and rely on their wands and spells to keep them at bay, which would only make matters worse...","open","base","worried","R")
    call ton_main("But that's not how I handle \"conflict\" with those beastly creatures...","base","base","base","mid")
    g9 "Yes?!"
    m "(I like where this is going!)"

    call nar(">*Fap!* *Fap!* *Fap!*")
    call ton_main("Centaurs don't do well with Ministry personnel{w} Even less so with female witches such as myself...","open","base","raised","mid")
    call ton_main("Making them a compelling offer so they'd peacefully return to their assigned territory was quite...{w} challenging {heart}","horny","base","base","R")
    g4 "Go on..."
    call ton_main("All I did was do them a small favour.{w} A little service the Ministry would never even think of providing them with.", "mad", "base", "worried", "down")
    call ton_main("But I did it anyway...","base","base","angry","mid")
    g4 "*Argh!* What did you do?"
    call ton_main("Well, I simply helped them release some of their stored up tension...","open","base","base","R")
    call ton_main("And stroked their manhoods with my hands...","horny","base","base","mid")

    g9 "Yes! How filthy!"
    call ton_main("*Hmph?!* You believe what I did was filthy, Professor?!", "base", "wide", "shocked", "stare")
    call ton_main("*Ehm*... I mean, it depends on how you look at it...","upset","base","worried","down")
    call ton_main("It's by far the simplest way to calm down a group of wild centaurs...","open","base","worried","R")
    call ton_main("As far as I could tell, they didn't have any females within their group...","open","base","base","mid")
    call ton_main("You can imagine the amount of tension that gets built up as a result of that...", "mad", "base", "base", "mid")
    call ton_main("(Inside those heavy, cum-filled balls!)","horny","base","base","ahegao", hair="horny") # ahegao
    m "So your idea was to jerk them off?"

    call ton_main("Well, yes.{w} They can't easily reach around to do it themselves now, can they?","horny","base","base","mid")
    m "(Those poor bastards!)"

    g4 "Must have been a real...{w}*argh*!- relief for them!"
    call ton_main("I believe so too, Sir.","base","base","base","mid")
    call ton_main("You should know, I never shy away from getting my hands dirty!","horny","base","raised","mid", hair="horny")
    g4 "*Agh!* Fuck! I'm getting close..."
    call ton_main("Most of the Ministry view Centaurs as \"lesser\" beings... As animals.","open","base","base","R")
    call ton_main("But not me. To me they're all powerful, and magnificent creatures.","base","base","angry","mid")
    call ton_main("And it's known that above all they embody strength, dominance, and lust...","open","base","base","mid")
    call ton_main("(And they are so{w} fucking{w} hung!!!)","horny","base","base","ahegao", hair="horny") # Ahegao

    #Genie cums
    stop music fadeout 1.0
    g4 "Yes! Here it comes!"

    call cum_block
    call gen_chibi("cum_behind_desk")
    with d3
    pause 1

    call ton_main("For a Ministry person to submit the way I did was quite the shock to them...","open","base","raised","R", hair="horny")

    call cum_block
    m "*Argh* You horse-cock-loving whore!"
    call ton_main("I have to say, Professor, now that I've told you.{w} I feel quite embarrassed about it!", "mad", "closed", "worried", "mid")

    call cum_block
    g4 "You dirty slut!"

    call ton_main("(I'd better not tell him what I had to do for their chieftain...)", "mad", "base", "worried", "L", hair="horny")
    call ton_main("(I can still taste him) {heart} {heart} {heart}","horny","base","base","ahegao", hair="horny")

    call hide_characters
    hide screen bld1
    with d3

    call gen_chibi("cum_behind_desk_done")
    with d3
    pause.5

    call bld
    g4 "(Fuck me, that felt great!)"

    call ton_main("A remarkable wizard such as yourself would never even consider solutions of such...","open","base","base","mid")
    call ton_main("Depravity...","horny","base","base","R", hair="horny")
    m "Are you asking me whether or not I'd jerk of a Centaur?..."
    m "Because that would be a clear \"no\" from me..."

    call ton_main("Professor, I've never told anybody about my experiences as an Auror...", "mad", "base", "worried", "down")
    m "Are there more \"experiences\" you could tell me about?"
    call ton_main("Well... I have been an Auror for quite a while now, so... I do have a couple.","open","base","worried","R")
    g9 "Great! I'd love to hear them!"

    jump end_tonks_hangout


    #(Not in use. Can be written into a Hangout event.)
    #ton "In fact I caught one of your teachers engaged in rather...{w=0.3} adulterous activities with a couple of students."
    #m "A couple...{w} Like, at the same time?"
    #ton "Panty pictures!"
    #m "What!"
    #ton "Well, I'm fine with any photographs really, ankles, butts, underwear..."
    #m "I see...{nw}
    #ton "Feet!"
    #g4 "Feet?"
    #ton "Well, anything I can get really."
    #m "(This lady's a pervert...)"
    #ton "There seems to be a great opportunity here..."
    #m "I'd rather keep my shoes on thank you!"
    #ton "Not that, silly."
