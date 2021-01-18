
# label purchase_forbidden_scroll(item):
#     hide screen weasley_store_menu
#     hide screen list_menu
#     with d3

#     if not hg_sex.trigger:
#         m "What's in this scroll?"
#         ger "Don't worry about it."
#         m "Why?"
#         ger "You're not ready for what's in this scroll."
#         m "Well, that just makes me want it more."
#         ger "Too bad, professor."
#         m "(Perhaps I should check it out later...)"
#         return

#     m "What's this scroll?"
#     fre "It is one of the components needed for a forbidden spell."
#     ger "Acquired completely legitimately I might add!"
#     m "What does it do?"
#     fre "It transforms you into... something."
#     m "Like what?"
#     fre "We don't know, it could be anything."
#     ger "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe inspiring dragon."
#     m "Not sure I'd really want to transform into any of those..."
#     ger "Well... those are just theories, we've not been able to use the scroll to find the second component ourselves."
#     m "Really? Now that's is surprising."
#     fre "Yes, although it's blank for some reason... not really anything new to us as we used to have a ma--"
#     ger "massive amounts of scrolls just like this one!"
#     ger "Yep... lot's of them, shame they all burnt."
#     fre "What are you-- *HHNG*"
#     fre "Oh! I see... Yes, very unfortunate..."
#     m "That is unfortunate... Well I'm sure I'll manage."
#     m "Ok, well how much is the scroll?"
#     ger "Five hundred gold coins."
#     g4 "Five hundred!? Why on earth is it so expensive?"
#     fre "Forbidden magic is quite a risky and expensive endeavour Professor, We'll sell it for no less than five hundred."

#     menu:
#         "-Buy the scroll ([item.cost] gold)":
#             if game.gold >= item.cost:
#                 m "Fine, here's the money"
#                 ger "Thank you very much"
#                 $ the_gift = item.get_image()
#                 show screen gift
#                 with d3
#                 $ game.gold -= item.cost
#                 $ item.unlocked = True

#                 ">Forbidden scroll has been added to your inventory."
#                 hide screen gift
#                 with d3
#             else:
#                 m "I don't have enough gold."
#                 fre "Perhaps later then."
#         "-No thanks-":
#             m "No thanks, not right now."
#             fre "Perhaps later then."

#     return
