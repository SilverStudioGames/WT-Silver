define loading_step_list = [
        "Spinning up disks",
        "Lubricating Hermione",
        "Filling up Tonks' glass",
        "Rendering Cho's marvellous abs",
        "Teaching Astoria some manners",
        "Gazing into the crystal ball",
        "Waxing Cho's broom",
        "Sanitizing Dumbledore's desk",
        "Confiscating Hermione's panties",
        "Adjusting the dress code",
        "Deleting Hermiobrine",
        "Initializing Snape walk physics",
        "Loading Genie's name mispronunciation engine",
        "Generating {s}dad{/s} bad jokes",
        "Perverting common nouns",
        "Inserting obscure pop culture references",
        "Loading wardrobe feature fondling",
        "Corrupting Teachers",
        "Ignoring plot holes",
        "Inflating Susan's tits",
        "Hiding Room of Requirement",
        "Predicting images",
        "Initializing sex-drive",
        "Loading loading screen",
        "Bribing ministry of magic employees",
        "Maximizing student gullibility levels",
        "Tuning out Luna's rambles",
        "Filling cupboard with trash",
        "Shredding rule violation reports",
        "Adding tissue box of holding to desk",
        "Ignoring established lore",
        "Neglecting minor characters",
        "Hiding the marauders map",
        "Injecting British slang",
        "Stiffening nipples",
        "Nickering at knickers",
        "Greasing Snape's hair",
        "Increasing Genie's imagination levels",
        "Adding illusion of choice dialogue options",
        "Redirecting blood flow",
        "Slutifying Slytherins",
        "Dampening Genie's powers",
        "Sleeving wizard cards",
        "Breaking old save files",
        "Loading pointless bird petting mechanics",
        "Applying desk chair cushioning charm",
        "Calculating semen trajectory",
        "Opening spank-bank account at Gringotts",
        "Scratching Genie's leg",
        "Polishing Genie's wand",
        "Defiling Cho's panties",
        "Eliminating common sense",
        "Applying lube",
        "Restocking chocolate frog supply",
        "Charming students",
        "Breaking the fourth wall",
        "Shortening skirts",
        "Undressing house-elves",
        "Lewdifying spells",
        "Inserting sexual innuendoes",
        "Searching for the g-spot",
        "Adjusting refractory period levels",
        "Indexing breast sizes",
        "Prolonging the inevitable heat death of the universe",
        "Redefining the big bang",
        "Insert disc 2"
        ]

init 1 python: # Needs to be appended AFTER update_savefile
    def load_assets():
        renpy.call_in_new_context("loading")
        return

    config.after_load_callbacks.append(load_assets)
    #config.per_frame_screens.append("loading")

label loading:
    call screen loading()
    $ renpy.block_rollback()
    return

screen loading():
    layer "interface"
    tag loading
    zorder 1000

    default step = 0
    default step_max = 7
    default steps = tuple(random.choice(loading_step_list) for _ in xrange(step_max+1))

    frame style "empty" background "#000"
    frame style "empty" background "#fff" maximum (406, 56) align (0.5, 0.5)
    bar value StaticValue(step, step_max):
        align (0.5, 0.5)
        maximum (400, 50)
        left_bar Frame(Solid("#ffffff"), 10, 0)
        right_bar Frame(Solid("#000000"), 10, 0)
        left_gutter 0
        right_gutter 0
        thumb None
        thumb_shadow None

    add "ch_hem reading" align (0.5, 0.92) zoom 0.45
    text "Loading" size 32 color "#ffffff" align (0.5, 0.4)
    text ("{}%".format(int(float(step) / step_max * 100))) size 32 color "#808080" align (0.5, 0.5)
    text ("{}".format(steps[step])) size 18 color "#808080" align (0.5, 0.6)

    timer 0.001 action SetScreenVariable("step", 1)

    if step is 1:
        add hermione.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 2)
    elif step is 2:
        add tonks.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 3)
    elif step is 3:
        add cho.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 4)
    elif step is 4:
        add astoria.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 5)
    elif step is 5:
        add luna.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 6)
    elif step is 6:
        add susan.get_image() alpha 0
        timer 0.001 action SetScreenVariable("step", 7)
    elif step is 7:
        if not renpy.predicting():
            timer 0.001 action Return()
