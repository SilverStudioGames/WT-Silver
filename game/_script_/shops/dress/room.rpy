label clothing_store:
    call room("clothing_store")
    call play_music("clothing_store")

    if mailbox.type_in_parcels("outfit"):
        maf "I'm sorry luv, but I'm still quite busy working on your previous order."
        maf "Come back once you received my package."
        jump return_office

    if not clothing_store_intro_done:
        $ clothing_store_intro_done = True

        ">You enter to see an old woman sewing together two pieces of long dark fabric."
        ">The woman is dressed almost entirely in pink and has a warm, approachable air to her."
        m "Hello."
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        m "Neither thank you, I'm just here to make a few inquiries."
        maf "Of course sir, what could I help you with?"
        m "Firstly, what type of items do you sell?"
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        m "I see. Do you ever make custom orders?"
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        m "So you're interested in making unique outfits?"
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colours at the moment."
        maf "What did you have in mind?"
        m "A few things. I haven't decided on anything specific yet."
        maf "Well, while you're making up your mind, feel free to browse the store."
    else:
        maf "What can I get you today?"

    $ gui.in_context("shop_dress")

    label clothing_store.end:

    m "Thank you very much."
    maf "You're welcome, sir. Come back any time."

    jump return_office

screen clothing_store():
    tag room_screen
    zorder 0

    if game.daytime:
        add "images/rooms/_bg_/corridor.webp" #Need day image.
    else:
        add "images/rooms/_bg_/corridor.webp"
