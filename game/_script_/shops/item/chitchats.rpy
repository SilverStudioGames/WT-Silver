label purchase_item(item):

    if item.currency == "tokens":
        if tokens < item.price:
            m "(I don't have enough tokens.)"
            return
    else:
        if game.gold < item.price:
            m "(I don't have enough gold.)"
            return

    if item == sealed_scroll_ITEM:
        if not hg_sex.trigger:
            m "What's in this scroll?"
            ger "Don't worry about it."
            m "Why?"
            fre "You're not ready for what's in this scroll."
            m "Well, that just makes me want it more."
            ger "Too bad, professor."
            m "(Perhaps I should check it out later...)"
            return

        m "I'd like to buy this scroll."
        ger "Five hundred gold coins."
        g4 "Five hundred!? Why on earth is it so expensive?"
        fre "Forbidden magic is quite a risky and expensive endeavour Professor, We'll sell it for no less than five hundred."
        m "What's it for anyway?"
        fre "It is one of the components needed for a forbidden spell."
        ger "Acquired completely legitimately I might add!"
        m "What does it do?"
        fre "It transforms you into... something."
        m "Like what?"
        fre "We don't know, it could be anything."
        ger "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe inspiring dragon."
        m "Not sure I'd really want to transform into any of those..."
        ger "Well... those are just theories, we've not been able to use the scroll to find the second component ourselves."
        m "Really? Now that's is surprising."
        fre "Yes, although it's blank for some reason... not really anything new to us as we used to have a ma--"
        ger "massive amounts of scrolls just like this one!"
        ger "Yep... lot's of them, shame they all burnt."
        fre "What are you-- *HHNG*"
        fre "Oh! I see... Yes, very unfortunate..."
        m "That is unfortunate... Well I'm sure I'll manage."

    elif item == poker_outfit_ITEM:
        $ item.used = True

        call unlock_clothing(">Congratulations! You have unlocked a new outfit!", her_outfit_poker)

    $ renpy.play("sounds/money.mp3")

    if item.currency == "tokens":
        $ tokens -= item.price
    else:
        $ game.gold -= item.price
    $ item.owned += 1

    return
