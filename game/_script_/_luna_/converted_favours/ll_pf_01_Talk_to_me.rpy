
# Luna (converted) talk to me
label luna_favour_1:

    m "{size=-4}(All I'll do is have a nice little conversation with her...){/size}"

    if lun_whoring == 0:
        # First time
        $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Okay then..."
        m "Tell me a little about yourself, [lun_name]."
        call lun_main("*Hmph*... I assume you'll be paying me for this [lun_genie_name].","normal","angry","angry","mid")
        menu:
            "-Five gold-":
                m "How does five gold sound [lun_name]?"
                call lun_main("five gold! Who do you think I am!","pout","mad","angry","mid")
                m "A student with no source of income."
                call lun_main("I am Luna Lovegood! You should be paying a hundred gold just to look at me!","upset","suspicious","mad","R")
                m "How does ten gold sound then?"
                call lun_main("Perhaps if you'd offered that to being with...","normal","angry","angry","mid")
                call lun_main("But now I'm far too upset to hold a conversation for such a low amount.","pout","angry","angry","R")
                m "would twenty gold calm you down?"
                call lun_main("well, I suppose it would.","base","closed","base","down")
                $ current_payout = 20
                m "Good, well now that we've got that sorted out..."
            "-Ten gold-":
                m "Will ten gold be enough for a conversation with your headmaster?"
                call lun_main("I suppose so...","normal","suspicious","base","mid")
                call lun_main("Just don't try anything funny.","upset","angry","angry","R")
                $ current_payout = 10
                m "Scout's honour. Now..."
            "-Fifty gold-":
                $ current_payout = 50
                m "How does fifty gold sound [lun_name]?"
                call lun_main("{size=+10}(FIFTY GOLD!){/size}","open_wide_tongue","wide","base","mid")
                call lun_main("*Hmph*... I suppose that's a fair amount.","base","happyCl","base","down")
                call lun_main("Just don't think it buys you anything other than a conversation.","normal","angry","angry","mid")
                m "Of course not. Speaking of which..."
        call lun_main("Fine, fine, I'll start...","normal","closed","base","down")
        call lun_main("My school life so far has been painfully dull.","upset","base","angry","mid")
        call lun_main("I've been under appreciated by everyone in this damn place.","normal","base","angry","R")
        call lun_main("No one seems to take me seriously...","normal","angry","angry","down")
        menu:
            "-Jerk off while she is talking-": # offended and stops unless you paid her 50 or offer to pay her more
                hide screen luna_main
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone
                with d3
                call gen_chibi("jerk_off_behind_desk")
                with d3
                call ctc

                call lun_main("what are you doing [lun_genie_name]!?","upset","suspicious","raised","mid")
                m "What, oh it's nothing. Simply adjusting my robe, that's all."
                if current_payout < 50:
                    call lun_main("This is exactly what I mean!","upset","mad","mad","mid")
                    call lun_main("Even the headmaster of this damn school thinks he can get away with touching himself in front of me for only {number=current_payout} gold!","upset","mad","mad","R")
                    call gen_chibi("sit_behind_desk")
                    with d3
                    "You quickly tuck your cock back into your robe."
                    m "i can assure you I was doing no such thing!"
                    call lun_main("whatever... I'm leaving","upset","mad","mad","R")
                    m "What! Already?"
                    call lun_main("Would you rather I stay and call the ministry of magic [lun_genie_name]?","upset","mad","mad","mid")
                    m "Fair enough."
                    call lun_main("I mean if you're going to try this on you could at least offer a little more than {number=current_payout} gold...","pout","suspicious","angry","mid")
                    jump luna_away
                call lun_main("...","normal","suspicious","base","R")
                call lun_main("{size=-5}(Well I suppose he did offer fifty gold...){/size}","base","suspicious","base","R")
                call lun_main("As I was saying, no one seems to even notice me.","normal","angry","angry","mid")
                call lun_main("The teachers are too busy playing favourites with the Gryffindor and Slytherin students.","pout","angry","angry","R")
                call lun_main("The girls are all self-obsessed.","upset","angry","angry","down")
                m "You don't say."
                call lun_main("and The boys are off chasing anything that shows a little skin...","upset","mad","angry","R")
                m "well, maybe you should fight fire with fire."
                call lun_main("what!? and parade myself around like some tart?","clench","wide","angry","R")
                m "{size=-4}(Yes... a nasty, little tart!){/size}"
                call lun_main("I bet you'd enjoy that wouldn't you [lun_genie_name]...","base","seductive","angry","mid")
                m "{size=-4}(Yes...){/size}"
                call lun_main("another one of your precious students, dressing like a slut.","base","seductive","base","R")
                m "{size=-2}(Yes......){/size}"
                call lun_main("showing off her body for anyone that will look.","smile","annoyed","angry","R")
                m "{size=+2}(Yes.........){/size}"
                call lun_main("You probably want me to act like those Slytherin sluts too...","base","suspicious","angry","mid")
                m "{size=+4}(Yes! Yes!){/size}"
                call lun_main("willing to show it all for a few points...","grin","suspicious","angry","mid")
                g4 "{size=+4}(almost there...){/size}"
                call lun_main("is that what you want [lun_genie_name]? a nice little Slytherin slut?","base","suspicious","angry","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                hide screen luna_main
                with d3
                call cum_block

                g4 "*Argh*! YES!"
                hide screen luna_main
                hide screen bld1
                call gen_chibi("cum_behind_desk")
                show screen bld1
                with d3

                call lun_main("That's it, [lun_genie_name], just let it all out...","base","seductive","base","mid")
                call gen_chibi("cum_behind_desk_done")
                with d3
                g4 "What? No, I was just... ah, shit, this feels good..."
                hide screen bld1
                with d3
                call lun_main("You couldn't help yourself could you?","base","seductive","raised","R")
                m "ah... I guess not."
                call lun_main("Well, I expect a bonus.","normal","happyCl","raised","R")
                m "I'm already paying you fifty gold!"
                call lun_main("That was just for the conversation. If you expect me to stand here and watch you cum all over yourself, that costs extra.","upset","mad","mad","R")
                m "Fine, I'll make it seventy gold."
                $ current_payout = 70
                call lun_main("Well I'm glad someone appreciates me.","base","seductive","raised","R")
                call lun_main("(Even if it is a filthy old pervert...)","normal","closed","raised","R")
            "-Participate in the conversation-":
                m "I can't see why..."
                call lun_main("Even my father doesn't treat me like he should.","normal","angry","angry","R")
                m "And how is that?"
                call lun_main("Like the princess I am!","pout","seductive","base","mid")
                m "(Not this again...)"
                call lun_main("As it is he's barely selling any copies of his newspaper.","upset","mad","mad","R")
                call lun_main("It's ridiculous! I should be showered in gifts and gold...","normal","suspicious","mad","R")
        call lun_main("Speaking of which...","normal","seductive","angry","mid")
        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna {number=current_payout} gold."
        call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    elif lun_whoring == 1:
        # Second time
        $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Alright then..."
        m "How's school going, [lun_name]."
        call lun_main("aren't we going to discuss how much you'll be paying me first, [lun_genie_name].","normal","angry","angry","mid")
        menu:
            "-Ten gold-": #just conversation (very short)
                $ current_payout = 10
                m "How does ten gold sound?"
                call lun_main("*Hmph*... Fine.","normal","closed","base","down")
                m "so about your school life..."
                call lun_main("School is boring. All I do is go to classes.","upset","base","angry","mid")
                call lun_main("Can I leave now?","normal","base","angry","R")
                g9 "What? That was barely a sentence!"
                call lun_main("And ten gold is barely a payment!","normal","base","angry","R")
                m "I'd say it's a fair payment for a little bit of idle chit chat."
                call lun_main("That's what you got. If you want more, pay more...","normal","base","mad","mid")
            "-Twenty gold-": #Slightly flirty, still short
                $ current_payout = 20
                m "Will twenty gold be enough for you, [lun_name]?"
                call lun_main("I suppose so...","normal","suspicious","base","mid")
                call lun_main("Just don't expect to get to touch yourself...","upset","angry","angry","R")
                m "How much would that cost?"
                call lun_main("...{w=0.5} More than twenty gold...","upset","angry","angry","R")
                m "Well I might take you up on that at a later date, For now tell me about school."
                call lun_main("School is boring...","upset","base","angry","mid")
                m "..."
                call lun_main("but there are a few interesting things happening... ","base","seductive","raised","mid")
                m "go on..."
                call lun_main("Well there are some rumours about Peeves the ghost...","base","seductive","raised","R")
                m "What sort?"
                call lun_main("Well I've heard that he's been touching some of the girls...","normal","seductive","sad","mid")
                m "How haven't I heard a complaint?"
                call lun_main("Well from what I hear... the girls don't have any complaints afterwards...","base","seductive","raised","mid")
                m "Ah... Anything else?"
                call lun_main("*Hmm*... nothing comes to mind.","normal","suspicious","angry","down")
                m "fair enough, well I think that was worth your twenty gold."
            "-One hundred gold-": #JOI
                $ current_payout = 100
                m "How about one hundred gold?"
                call lun_main("Fine...","normal","seductive","angry","R")
                call lun_main("...","normal","suspicious","angry","mid")
                call lun_main("......","upset","suspicious","raised","mid")
                call lun_main("Well are you going to start?","upset","mad","mad","R")
                m "Start what? You're the one who's supposed to be talking."
                call lun_main("Oh please... You expect me to believe you're willing to pay your students a hundred gold just to talk?","upset","angry","raised","mid")
                m "Well I suppose that--"
                call lun_main("Just start stroking your cock already [lun_genie_name].","normal","seductive","base","mid")
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone
                with d3
                call gen_chibi("jerk_off_behind_desk")
                with d3
                pause
                call lun_main("Isn't that better?","base","seductive","raised","mid")
                m "..."
                call lun_main("So do you pay anyone else to watch you sit there and jerk your filthy old cock?","upset","seductive","angry","mid")
                m "{size=-4}(I guess I don't really pay hermione...){/size}"
                m "ah... no..."
                call lun_main("good...","base","seductive","base","R")
                m "Good?"
                call lun_main("Well... we can't have you wasting your money on any of those other little tarts can we?","upset","mad","mad","mid")
                menu:
                    "-Play along-": #act submissive
                        $ lun_dom += 1
                        $ current_payout = 150
                        m "ah... of course not..."
                        call lun_main("That's right... why bother with them when I'm here to talk with you...","base","mad","mad","mid")
                        m "{size=-4}(Yes...){/size}"
                        call lun_main("That's it, keep stroking it for me [lun_genie_name].","normal","suspicious","angry","mid")
                        m "{size=-4}(Yes... yes...){/size}"
                        call lun_main("It's probably I good thing that I watch you drain your balls.","normal","suspicious","angry","R")
                        call lun_main("Otherwise, who knows who you might call up here to watch you do it...","pout","angry","angry","mid")
                        m "{size=-4}(*mmmm*... yes...){/size}"
                        call lun_main("You'd probably even do it in front of a first year, wouldn't you?","base","suspicious","angry","mid")
                        ">You stop stroking your cock."
                        m "I'd never do any--"
                        call lun_main("Do you even know how old I am?","base","suspicious","raised","mid")
                        m "of course..."
                        call lun_main("*Hmph*... Are you sure about that?","soft","angry","raised","mid")
                        m "..."
                        call lun_main("Back to stroking it [lun_genie_name]...","base","suspicious","mad","mid")
                        ">You start stroking your cock again."
                        call lun_main("Doesn't that feel better?","base","suspicious","mad","R")
                        m "{size=-4}(*Argh*... yes...){/size}"
                        call lun_main("Say it out loud.","base","mad","mad","mid")
                        m "{size=-4}yes...{/size}"
                        call lun_main("Good. Now cum for me.","base","suspicious","angry","mid")
                        m "{size=-2}(What?){/size}"
                        call lun_main("come on...","base","suspicious","sad","mid")
                        g4 "{size=+4}(*agh*... almost there...){/size}"
                        call lun_main("Come for me...","soft","angry","mad","mid")
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                        hide screen luna_main
                        with d3
                        call cum_block

                        g4 "*Argh*! YES!"
                        hide screen luna_main
                        hide screen bld1
                        call gen_chibi("cum_behind_desk")
                        show screen bld1
                        with d3

                        call lun_main("That's it, [lun_genie_name] just like that...","base","seductive","base","mid")
                        call gen_chibi("cum_behind_desk_done")
                        with d3
                        g4 "What? No, I was thinking about... ah, shit, this feels too good..."
                        hide screen bld1
                        with d3
                        call lun_main("Your a nasty old man, aren't you.","base","seductive","raised","R")
                        m "ah..."
                        call lun_main("Don't worry, I won't tell anyone...","base","seductive","raised","mid")
                        m "Thank you..."
                        call lun_main("I expect to be fairly compensated however...","base","angry","angry","R")
                        m "Don't worry, I'll add an extra fifty gold to your payment."
                        call lun_main("That's the least you could do [lun_genie_name]...","base","suspicious","raised","R")

                    "-Let her know her place-": #note that he could get more for less from those tarts
                        $ lun_sub += 1
                        m "well now that you mention it I'm sure those tarts would probably charge a lot less for a conversation..."
                        call lun_main("*Hmph*... You get what you pay for.","upset","angry","mad","R")
                        m "And what exactly am I getting from you for my payment?"
                        call lun_main("Getting to Look at me while you stroke your filthy old cock should be payment enough.","normal","angry","mad","mid")
                        m "Well you'll have to excuse my old eyes because I can barely see you..."
                        menu:
                            m "..."
                            "-Ask her to open her top-":
                                $ lun_sub += 1
                                m "Perhaps you should undo a button or two so I can get a better look."
                                call lun_main("Are you serious? You expect me to flaunt myself like some cheap tart?","normal","mad","angry","mid")
                                m "No, I expect you to flaunt yourself like the princess you claim to be..."
                                call lun_main("...","normal","angry","angry","R")
                                m "I'm waiting..."
                                call lun_main("... {size=-8}(fine...){/size}","upset","suspicious","sad","down")
                                ">Luna removes her tie and opens her top slightly..."
                                hide screen luna_main
                                with d3

                                $ lun_top_level = 2
                                call set_lun_top("top_2_r")

                                call lun_main("...","normal","suspicious","sad","down")
                                m "Why don't you keep you're shirt like that from now on..."
                                call lun_main("...","upset","suspicious","sad","R")

                            "-Ask her to come closer-":
                                m "Perhaps you should come stand a little closer."
                                call lun_main("Really? You want me to come closer while you...?","normal","suspicious","mad","mid")
                                m "Well I am so \"old\"..."
                                call lun_main("...","normal","angry","angry","R")
                                m "I'm waiting..."
                                call lun_main("... {size=-8}(fine...){/size}","upset","suspicious","sad","down")

                                call lun_walk("desk")

                                m "Very good... Maybe you should stand this close from now on..."
                                call lun_main("...","upset","suspicious","sad","R")


                        call lun_main("Is this what you want?","upset","suspicious","sad","down")
                        call lun_main("To humiliate me...","upset","suspicious","mad","mid")
                        m "{size=-4}(*mmmm*... yes...){/size}"
                        call lun_main("You love this, don't you...","normal","angry","angry","mid")
                        ">You start stroking faster."
                        call lun_main("What I'm forced to do...","normal","angry","mad","down")
                        call lun_main("Just to survive...","upset","suspicious","sad","down")
                        m "..."
                        call lun_main("Well don't worry about that...","normal","mad","mad","mid")
                        call lun_main("Just keep stroking it.","base","mad","mad","R")
                        m "{size=-4}(*Argh*... yes...){/size}"
                        call lun_main("You nasty old man","base","mad","mad","mid")
                        m "{size=-4}yes...{/size}"
                        call lun_main("Get your moneys worth...","upset","suspicious","mad","mid")
                        m "{size=-2}(*mmmm*...){/size}"
                        call lun_main("come on...","base","suspicious","angry","mid")
                        g4 "{size=+4}(*agh*... almost there...){/size}"
                        call lun_main("come for your poor student...","base","suspicious","sad","mid")
                        g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"
                        hide screen luna_main
                        with d3
                        call cum_block

                        g4 "*Argh*! YES!"
                        hide screen luna_main
                        hide screen bld1
                        call gen_chibi("cum_behind_desk")
                        show screen bld1
                        with d3

                        call lun_main("That's it, just let it out...","upset","mad","mad","mid")
                        call gen_chibi("cum_behind_desk_done")
                        with d3
                        g4 "good work, slut... ah, shit, this feels so good..."
                        hide screen bld1
                        with d3
                        call lun_main("Your a nasty old man, aren't you.","base","suspicious","raised","mid")
                        m "ah..."
                        call lun_main("Forcing me to watch you do this...","base","suspicious","mad","R")
                        m "Ah... I'm not forcing you to do anything..."
                        call lun_main("*Hmph*... well I expect to be paid now...","normal","mad","angry","mid")
                        m "Don't worry, I'll give you your hundred gold."
                        call lun_main("*Hmph*... Fine...{w=0.5} (Nothing extra...?)","upset","mad","angry","R")


        call lun_main("Speaking of which...","normal","seductive","angry","mid")
        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna {number=current_payout} gold."
        call lun_main("Thank you, [lun_genie_name].","base","seductive","base","R")
        ">Luna leaves your office."

    elif lun_whoring >= 2 and lun_whoring < 13:
        # Third time
        if lun_whoring <= 2:
            $ lun_whoring += 1
        call play_music("chipper_doodle")
        m "Tell me [lun_name]..."
        m "How's you're home life going?"
        call lun_main("My home life?","normal","angry","raised","R")
        call lun_main("In one word, [lun_genie_name], inadequate.","pout","angry","angry","mid")
        m "inadequate?"
        call lun_main("Yes! Someone such as myself should be showered with gifts and gold.","pout","mad","angry","R")
        call lun_main("Instead I live in a chess piece while my stupid, worthless father struggles to sell ten copies of his dumb paper!","upset","mad","mad","down")
        m "Surely he sells more than ten copies?"
        call lun_main("Barely...","normal","angry","angry","R")
        call lun_main("He's struggling to get any institutions to stock it these days... ever since the ministry stopped buying it.","normal","suspicious","angry","R")
        menu:
            "-Say nothing-": #act submissive
                if lun_dom <= 1:
                    $ lun_dom += 1
                $ current_payout = 150
                call lun_main("Wait... that's it!","base","seductive","angry","mid")
                m "what's it?"
                call lun_main("Why don't you start buying \"the Quibbler\" [lun_genie_name]?.","base","seductive","base","mid")
                m "I hardly think one more person is going to turn things around."
                call lun_main("Not you personally [lun_genie_name], Hogwarts!","normal","mad","angry","mid")
                call lun_main("Just imagine how many copies the entire school would buy!","smile","base","angry","R")
                m "*Hmm*... I'll think about it."
                call lun_main("You'll {size=+4}think{/size} about it?","upset","suspicious","mad","mid")
                call lun_main("*Hmph*... Maybe I'll just have to {size=+4}think{/size} about getting my father to write a story...","upset","suspicious","mad","R")
                call lun_main("involving a perverted old headmaster who likes to lure girls into his office...","upset","suspicious","raised","R")
                call lun_main("Just to leer at them while he strokes his filthy old cock...","upset","suspicious","angry","mid")
                m "..."
                call lun_main("I'm sure that would sell some extra copies...","upset","mad","raised","R")
                call lun_main("Well?","normal","suspicious","mad","mid")
                m "Fine, fine. I'll get someone to start ordering some extra copies for the library."
                call lun_main("There, isn't that easy?","base","seductive","angry","R")
                m "yes..."
                call lun_main("Good. Now as a reward, I'll let you touch that filthy old cock of yours.","base","angry","angry","mid")
                m "..."
                call lun_main("come on [lun_genie_name]...","base","suspicious","sad","mid")
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone
                with d3
                call gen_chibi("jerk_off_behind_desk")
                with d3
                pause
                call lun_main("That's better isn't it?","base","suspicious","angry","mid")
                call lun_main("Just listen to my voice while you stroke yourself...","base","suspicious","angry","R")
                m "..."
                call lun_main("Just think about how happy I'll be once father becomes a respectable member of society.","base","mad","mad","mid")
                call lun_main("Think about how much you enjoy making me happy...","base","mad","mad","R")
                m "{size=-4}(*Argh*... yes...){/size}"
                call lun_main("You love making me happy don't you [lun_genie_name]...","base","mad","mad","mid")
                m "{size=-4}yes...{/size}"
                call lun_main("say it louder...","base","mad","mad","mid")
                m "yes..."
                call lun_main("It makes you feel so good doesn't it...","base","suspicious","mad","mid")
                m "{size=-2}(*mmmm*...){/size}"
                m "{size=+2}yes...{/size}"
                call lun_main("maybe I'll even make you kiss my feet... that would make me very happy","base","suspicious","angry","mid")
                g4 "{size=+4}(*agh*...){/size}"
                g4 "{size=+4}yes...{/size}"
                call lun_main("that's it [lun_genie_name], cum for your princess...","base","suspicious","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                g4 "{size=+4}(*agh*... almost there...){/size}"
                call lun_main("cum...","soft","angry","mad","mid")
                call lun_main("{size=+4}cum!{/size}","soft","angry","mad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                hide screen luna_main
                with d3
                call cum_block

                g4 "*Argh*! YES!"
                hide screen luna_main
                hide screen bld1
                call gen_chibi("cum_behind_desk")
                show screen bld1
                with d3

                call lun_main("That's it, [lun_genie_name] just like that...","normal","mad","angry","mid")
                call gen_chibi("cum_behind_desk_done")
                with d3
                g4 "ah, shit, why does this feels so good..."
                hide screen bld1
                with d3
                call lun_main("Disgusting...","clench","seductive","base","R")
                m "ah..."
                call lun_main("...","normal","mad","angry","mid")
                m "Thank you..."
                call lun_main("Thank you...?","upset","suspicious","mad","mid")
                m "Thank you princess..."

                $ lun_name = "Princess"

                call lun_main("That's better [lun_genie_name]...","base","angry","angry","mid")
                call lun_main("Now as a princess I expect a present for having to look at such a filthy act...","base","angry","angry","R")

            "-Make an offer-": #exchange quibbler purchase
                if lun_sub <= 1:
                    $ lun_sub += 1
                $ current_payout = 50
                m "well I'm sure that I could have a few words with the library staff about stocking it..."
                call lun_main("Really? You'd do that?","base","wide","base","mid")
                m "Of course."
                call lun_main("Thank you so much [lun_genie_name]!","base","happyCl","base","mid")
                m "I was thinking you could thank me for my generous offer another way..."
                call lun_main("Oh...","upset","angry","mad","R")
                m "That's not a problem is it [lun_name]?"
                call lun_main("Of course not... What did you have in mind?","normal","suspicious","sad","down")
                m "well for starters..."
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone
                with d3
                call gen_chibi("jerk_off_behind_desk")
                with d3
                call ctc

                menu:
                    "-Ask her to shorten her skirt-":
                        if lun_sub <= 2:
                            $ lun_sub += 1
                        m "let's talk about that skirt of yours..."
                        call lun_main("What about it?","normal","mad","angry","mid")
                        m "have you ever considered wearing it a little... shorter?"
                        call lun_main("...","normal","angry","angry","R")
                        m "I'm waiting..."
                        call lun_main("... how short?","upset","suspicious","sad","down")
                        m "Just an inch or so higher."
                        call lun_main("...","upset","suspicious","sad","down")
                        call lun_main("(my father better appreciate this...)","upset","suspicious","sad","down")
                        ">Luna pulls up her skirt slightly and then folds it over at the top..."
                        hide screen luna_main
                        with d3

                        $ lun_skirt_level = 2
                        call set_lun_bottom("skirt_2")

                        call lun_main("...","upset","suspicious","sad","down")
                        m "{size=-4}(*mmmm*... yes...){/size}"
                        m "Why don't you wear it like that from now on..."
                        call lun_main("yes, [lun_genie_name].","upset","suspicious","sad","R")

                    "-Make her call you sir-":
                        $ lun_genie_name = "Sir"
                        m "How about you start giving me the respect I deserve."
                        call lun_main("...","normal","suspicious","mad","mid")
                        m "I want you to refer to me as sir from now on."
                        call lun_main("...","normal","angry","angry","R")
                        m "Is that clear?"
                        call lun_main("... Yes...{size=-8}sir{/size}","upset","suspicious","sad","down")
                        m "Speak up [lun_name]..."
                        call lun_main("Yes sir...","upset","suspicious","sad","R")
                        m "{size=-4}(yes...){/size}"


                call lun_main("You know this is wrong don't you?","upset","suspicious","sad","down")
                call lun_main("What you're forcing me to do...","upset","suspicious","mad","mid")
                m "{size=-4}(*mmmm*... yes...){/size}"
                m "I don't recall forcing you into anything [lun_name]..."
                call lun_main("*Hmph*...","normal","angry","angry","mid")
                ">You start stroking faster."
                call lun_main("Well...","normal","angry","mad","down")
                call lun_main("Just get it over with...","upset","suspicious","sad","down")
                m "{size=-4}ah...{/size}"
                call lun_main("Just keep touching yourself in front of me...","normal","mad","mad","mid")
                m "{size=-4}(*Argh*... Yes...){/size}"
                call lun_main("Let it all out front of me...","grin","mad","mad","mid")
                m "{size=-4}Yes...{/size}"
                call lun_main("Your student...","upset","suspicious","mad","mid")
                m "{size=-2}(*Mmmm*...){/size}"
                call lun_main("come on...","base","suspicious","angry","mid")
                g4 "{size=+4}(*Argh*... almost there...){/size}"
                call lun_main("Come for your little princess...","base","suspicious","sad","mid")
                g4 "{size=+4}(YES! YES! YES!) *Argh*!{/size}"
                hide screen luna_main
                with d3
                call cum_block

                g4 "*Argh*! YES!"
                hide screen luna_main
                hide screen bld1
                call gen_chibi("cum_behind_desk")
                show screen bld1
                with d3

                call lun_main("*Ugh*... There's so much...","upset","mad","mad","mid")
                call gen_chibi("cum_behind_desk_done")
                with d3
                g4 "Good work, slut... ah, shit, this feels so good..."
                hide screen bld1
                with d3
                call lun_main("The floor...","normal","angry","angry","down")
                call lun_main("It's covered...","normal","angry","angry","R")
                m "*Ah*... you did good [lun_name]..."
                call lun_main("*Hmph*... Well I expect to be paid now...","normal","mad","angry","mid")


        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna {number=current_payout} gold."
        call lun_main("Thank you, [lun_genie_name].","normal","seductive","base","R")
        if current_payout <= 50:
            call lun_main("(only {number=current_payout}?) *Hmph*","upset","mad","angry","R")
        ">Luna leaves your office."

    else:
        # Repeatable, Hermione joins in
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
        m "Tell me [lun_name]..."
        m "How's your tutoring with Miss Granger going?"
        call lun_main("my lessons with hermione?","normal","angry","angry","R")
        call lun_main("Honestly... they're fantastic.","base","base","base","down")
        m "really?"
        call lun_main("Yes... at first I thought that they'd just be a waste of time...","normal","mad","sad","R")
        call lun_main("but they're actually helping a lot.","base","base","sad","mid")
        m "*mmmmm*, the way you sucked my cock is proof enough of that..."
        call lun_main("*Hmph* I meant my grades...","normal","angry","angry","R")
        call lun_main("Although she has been a great help with sex as well...","base","seductive","angry","down")
        call lun_main("in fact... Why don't you bring her up here now?","base","seductive","angry","mid")
        m "why?"
        call lun_main("well I think we both know you only started this conversation so you could stroke your filthy cock of your while I speak...","base","angry","angry","mid")
        m "maybe..."
        call lun_main("why not bring hermione up here for a little more fun?","base","mad","angry","mid")
        call lun_main("we might even give you something to look at...","base","seductive","angry","R")
        m "done!"

        ">you quickly summon hermione up to your office."
        call play_sound("door")
        call her_chibi("stand","desk","base")
        hide screen luna_main
        $ luna_r_arm = 2
        call lun_main(xpos=390, flip=True)
        with d3

        call update_her_uniform
        pause.8

        call her_main("Hello Professor!", "base", "happyCl", "base", "mid", xpos="base", ypos="base")
        call her_main("Hi Luna! what's he want now? another blowjob.", "grin", "base", "base", "R")
        call lun_main("no, he just wants to talk...","base","seductive","angry","mid")
        call her_main("really?", "upset", "wink", "base", "mid")
        call lun_main("I mean he says talk...","normal","angry","mad","R")
        call lun_main("but I think we both know he wants to sit there and stroke that filthy old cock of his while we do all the talking.","base","seductive","angry","mid")
        call her_main("typical...", "base", "narrow", "worried", "down")
        call her_main("so what did you want me here for?", "base", "narrow", "base", "mid_soft")
        call lun_main("I figured you could lend a hand... plus this way we both get paid.","normal","angry","angry","R")
        call her_main("*Aww*, that's so sweet Luna!", "base", "happyCl", "worried", "mid")
        call lun_main("Well, it's more like I want a lesson on dirty talk...","normal","mad","sad","R")
        call her_main("whatever you say... now I think it's about time you started stroking that cock of yours don't you [genie_name]?", "base", "narrow", "base", "mid_soft")
        call lun_main("yeah, come on [lun_genie_name]...","base","seductive","sad","mid", flip=False)
        m "I'm not going to say no to that am I?"
        hide screen blktone
        with d3
        ">You reach under the desk and grab your cock..."
        hide screen blktone
        with d3
        call gen_chibi("jerk_off_behind_desk")
        with d3
        pause
        call lun_main("That's better isn't it?","normal","angry","sad","mid")
        call lun_main("Just listen to our voices while you stroke yourself...","base","mad","angry","mid")
        call her_main("*mmmm*... he loves it when you tell him a story...", "base", "squint", "base", "mid")
        call lun_main("Really? What sort?","base","seductive","sad","R")
        call her_main("how about the time we nearly got caught during blowjob practice...", "base", "narrow", "worried", "down")
        call lun_main("What? Not that one!","open","wide","sad","mid", flip=True)
        m "What happened?"
        call lun_main("It's too embarrassing! I'm not telling him that one!","open","wide","sad","R", flip=False)
        call her_main("well I don't mind...", "open", "base", "base", "R")
        call lun_main("please hermione...","normal","wide","sad","mid", flip=True)
        call her_main("*shhh*...", "open", "closed", "base", "mid")
        m "go on..."
        ">you speed up your stroking."
        call her_main("the other evening, Luna and I were busy studying after class as usual...", "soft", "happy", "base", "R")
        call lun_main("...","upset","wide","sad","down", cheeks="blush", flip=False)
        m "..."
        call her_main("we'd just finished up basic spells revision so we moved onto blowjobs as usual...", "open", "base", "base", "R")
        call lun_main("...","normal","wide","sad","R", cheeks="blush")
        m "{size=-2}(*mmmm*...){/size}"
        call her_main("it was going well when all of a sudden a few second years came into the common room...", "angry", "wink", "base", "mid")
        call lun_main("you said it was going to be empty!","normal","wide","sad","mid", cheeks="blush")
        call her_main("it was incredible sir... she swallowed the whole thing...", "base", "narrow", "worried", "down")
        g4 "{size=+4}(*agh*...){/size}"
        g4 "{size=+4}yes...{/size}"
        call her_main("she hid all 6 inches of it in her mouth... down her throat...", "base", "narrow", "base", "mid_soft")
        call her_main("just so we wouldn't get found out...", "base", "squint", "base", "mid")
        call lun_main("well what else was I supposed to do...","open","wide","sad","mid", cheeks="blush", flip=True)
        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
        g4 "{size=+4}(*agh*... almost there...){/size}"
        call lun_main(flip=False)
        call her_main("she held it there for nearly a minute...", "open", "base", "base", "R")
        call her_main("a few of them even said hello to us...", "soft", "happy", "base", "R")
        call her_main("they didn't suspect a thing...", "soft", "narrow", "annoyed", "up")
        call lun_main("not until you started touching me under the desk!","normal","wide","angry","R", cheeks="blush")
        g4 "{size=+4}*Argh*! yes you whores!{/size}"
        hide screen luna_main
        with d3
        call cum_block

        g4 "*Argh*! YES!"
        hide screen luna_main
        hide screen bld1
        call gen_chibi("cum_behind_desk")
        show screen bld1
        with d3

        call lun_main("...","base","seductive","sad","mid", cheeks="blush")
        call her_main("I told you he liked stories...", "base", "narrow", "base", "mid_soft")
        call gen_chibi("cum_behind_desk_done")
        with d3
        g4 "Ah shit, why does this feel so good..."
        hide screen bld1
        with d3

        call lun_main("next time just make one up...","upset","seductive","angry","R")
        m "*ah*..."
        call her_main("come on Luna, we've got to earn our payment, speaking of...", "base", "squint", "base", "mid")

        m "Alright, alright. Here's your gold and points."
        $ gryffindor += 15
        $ ravenclaw += 15
        m "Fifteen points to Gryffindor and Ravenclaw."
        $ gold -= 50
        $ luna_gold += 25
        m "Here's your gold."
        ">You hand Luna and hermione twenty-five gold each."
        call her_main("Thank you [genie_name]!", "base", "base", "base", "mid")
        call lun_main("... Thank you sir.","normal","seductive","sad","R")
        ">Luna and hermione leave your office, talking as they go."

        $ hermione_busy = True


    hide screen hermione_main
    hide screen luna_main
    with d3

    call gen_chibi("sit_behind_desk")
    pause.2

    call play_sound("door")
    call lun_chibi("hide")
    call her_chibi("hide")

    $ luna_busy = True

    jump main_room
