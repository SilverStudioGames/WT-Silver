
default quidditchguide_ITEM = Item("general", "book", "Quidditch Guide", 200, "This book contains the basic knowledge of Quidditch.", label="quidditch_guide_book", limit=1)

default galadriel1_ITEM = Item("galadriel1", "book", "Tome 1: The Tale of Galadriel", 100, "This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny.\nEffect: Improves imagination.", label="galadriel1_book", limit=1)
default galadriel2_ITEM = Item("galadriel2", "book", "Tome 2: The Tale of Galadriel", 200, "This is a continuation on the story of the elven princess who defies the tradition, with a twist.\nEffect: Improves imagination.", label="galadriel2_book", limit=1, unlocked=False)

default gameofchairs1_ITEM = Item("game_of_chairs1", "book", "Tome 1: Game of Chairs", 200, "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.", label="game_of_chairs1_book", limit=1)

label book_start:
    call weather_sound
    call play_music("stop")
    call play_sound("bookopen")

    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
        hide screen chair_right
        call gen_chibi("read_near_fire")
        with d3
    else:
        hide screen chair_right
        call gen_chibi("read")
        with d3
    return

label book_end:
    call play_sound("bookclose")

    if fire_in_fireplace:
        call gen_chibi("read_near_fire_done")
    else:
        call gen_chibi("read_done")
    return

label galadriel1_book:
    call book_start

    nar "Galadriel - a gentle and gracious elven princess is introduced into the story."
    nar "Galadriel's father - King Methis, and his childhood friend Mofothelis are introduced into the story."
    nar "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis."
    nar "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle."
    nar "King Methis dismisses her daughter's {i}foolish{/i} complaints. Galadriel decides to run away."
    nar "Galadriel manages to leave the royal residence at night unnoticed..."
    nar "King Methis is furious about his daughter's escape. He decides to personally lead the search party."
    nar "Galadriel rides her mare named {i}white dove{/i} through the forest. The Princess enjoys her freedom..."
    nar "After a while she meets a rather handsome human nobleman on a horse..."
    nar "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries, occasionally interrupted with laughter."
    nar "Suddenly the nobleman attacks the princess and knocks her out!"
    nar "When Galadriel comes to, to her horror, she realises that the nobleman is having his way with her."
    nar "Galadriel is screaming for help but the man only laughs at her."
    nar "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously."
    nar "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop."
    nar "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen."
    nar "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage."
    nar "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food."
    nar "Galadriel is starting to feel hopeful but it does not last. Soon she realises what kind of establishment this is: a whorehouse."
    nar "The elven princess is forced to work as a whore. She detests her new life but has very little choice."
    nar "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasionally dwarfs - she spreads her legs for everyone."
    nar "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel."
    nar "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant."
    nar "The end."

    call book_end

    m "What the fuck did I just read?"

    if game.daytime:
        jump night_start
    else:
        jump day_start

label galadriel2_book:
    call book_start

    nar "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly."
    nar "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel."
    nar "The Elven Royal-Whore knows nothing of the life outside the walls of the brothel. But it does not affect her determination to escape."
    nar "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel."
    nar "Galadriel soon gets lost in the vast city and is forced to spend the night on the street."
    nar "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly."
    nar "The now pregnant Galadriel offers her {i}company{/i} to a couple of filthy-looking homeless men in exchange for food. She spends the night with them."
    nar "Galadriel realises that her life back in the brothel wasn't so bad compared to the live she's been leading for the past several days. She decides to return."
    nar "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back."
    nar "Galadriel is, yet again, warm, fed and full of cum. She is glad to be back and as popular as ever."
    nar "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now..."
    nar "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him."
    nar "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her."
    nar "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off."
    nar "Galadriel recognises the man as her father - King Methis. Only now he realises that the pregnant whore he fucked for hours is his long lost daughter."
    nar "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face..."
    nar "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed."
    nar "It takes the elven princess several minutes to realise that she never was pregnant. The entire adventure was nothing but a dream."
    nar "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis."
    nar "Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite."
    nar "The end."

    call book_end

    m "..."

    if game.daytime:
        jump night_start
    else:
        jump day_start

label game_of_chairs1_book:
    call book_start

    nar "A family of noble northmen is introduced into the story."
    nar "The royal family and the king are introduced into the story."
    nar "Another family is introduced into the story."
    nar "Some incest action between a brother and his sister, the queen, is taking place."
    nar "Attempted child murder takes place. The kid barely survives and is now in a coma."
    nar "Some more characters are introduced into the story."
    nar "Some characters hatch an evil scheme against some other characters."
    nar "The king gets poisoned and dies, his wife is cheering."
    nar "Some more brother on sister action takes place."
    nar "A certain character you've been especially rooting for gets executed."
    nar "Some new characters are introduced into the story."
    nar "Some female characters get raped and then killed brutally."
    nar "Some more members of the noble family of northmen find their untimely demise."
    nar "Some more women get raped. Some of them manage to survive."
    nar "The characters you hate clash in an epic battle against the characters you are rooting for."
    nar "Most of the characters you hate survive the battle. Every single character you were rooting for is dead."
    nar "Some more rapes take place, then some more murders..."
    "> You don't even care anymore."
    nar "A new group of characters is introduced into the story. You sort of starting to root for one of them."
    nar "The character you were rooting for falls in love with a pretty girl."
    nar "The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well."
    nar "A new race of half-frozen undead monsters is introduced into the story."
    nar "The end."

    call book_end

    m "The author of this book has some serious issues."
    m "I wonder if it's even worth picking up the continuation..."

    if game.daytime:
        jump night_start
    else:
        jump day_start

label quidditch_guide_book:
    call book_start

    nar "Quidditch - One of the most popular sports in the wizarding world is a team based sport played on broomsticks..."
    nar "Two opposing teams with seven people making up each team go up against each other..."
    nar "The game is played using four balls... One quaffle, two bludgers and one snitch.\nThe beginning of the match is signalled by the quaffle being thrown into the air by the referee..."
    nar "Quidditch, unlike many other sports is played on an oval shaped pitch with a scoring area on each end..."
    nar "Much like other sports, you're not allowed to go outside the boundary lines with the quaffle or you'd have to hand it over to the opposing team..."
    nar "When the game is set in motion each player takes their assigned positions.\nThere's three chasers, two beaters, one keeper and one seeker..."
    nar "The chasers purpose is to score the Quaffle. Beaters on the other hand is to hit them with the bludgers as to knock the ball out of their grasp... The keeper blocks the goal and the seeker needs to catch the snitch."
    nar "As most injuries are easily remedied through magical means there's nothing to stop a player from knocking into one another as to get a hold of the Quaffle. Distraction tactics are also common even during official matches..."
    nar "The way scoring is done is when the chaser has a hold of the quaffle they need to get to the opponent's side of the pitch and score it by getting it through a hoop..."
    nar "The winning team is decided once the snitch is caught which is worth 150 points to the team of which seeker caught it. Therefore a match could technically go on forever... The longest Quidditch match went on for about 3 months..."

    call book_end

    m "Bludgers and quaffles?"
    m "This is even more stupid than I imagined."

    if game.daytime:
        jump night_start
    else:
        jump day_start
