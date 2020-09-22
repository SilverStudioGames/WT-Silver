# Narrator (not the same as 'nar' character)
label nar(text="", action=""):

    if action != "end": #Narration ended, blktone was already active.
        show screen blktone5
        with d3

    if text != "":
        "[text]"

    if action != "start": #Narration just started, blktone won't get hidden.
        hide screen blktone5
        with d3

    return

define gen = Character("Genie")
define m = Character(None, show_side_image=Image("characters/genie/mage.webp", xpos=20))
define g2 = Character(None, show_side_image=Image("characters/genie/mage2.webp", xpos=20))
define g3 = Character(None, show_side_image=Image("characters/genie/mage3.webp", xpos=20))
define g4 = Character(None, show_side_image=Image("characters/genie/mage4.webp", xpos=20))
define g5 = Character(None, show_side_image=Image("characters/genie/mage5.webp", xpos=20))
define g6 = Character(None, show_side_image=Image("characters/genie/mage6.webp", xpos=20))
define g7 = Character(None, show_side_image=Image("characters/genie/mage7.webp", xpos=20))
define g8 = Character(None, show_side_image=Image("characters/genie/mage8.webp", xpos=20))
define g9 = Character(None, show_side_image=Image("characters/genie/mage9.webp", xpos=20))
define g10 = Character(None, show_side_image=Image("characters/genie/mage10.webp", xpos=20))
define g11 = Character(None, show_side_image=Image("characters/genie/mage11.webp", xpos=20))
define g12 = Character(None, show_side_image=Image("characters/genie/mage12.webp", xpos=20))
define g13 = Character(None, show_side_image=Image("characters/genie/mage13.webp", xpos=20))
define g14 = Character(None, show_side_image=Image("characters/genie/mage14.webp", xpos=20))
define g15 = Character(None, show_side_image=Image("characters/genie/mage15.webp", xpos=20))
define g16 = Character(None, show_side_image=Image("characters/genie/mage16.webp", xpos=20))

# Students
# (Cho is added to character store to avoid variable name conflict with Doll object instance)
define character.cho = Character("[cho_name]", predict_function=doll_prediction("cho"))
define her = Character("[hermione_name]", predict_function=doll_prediction("hermione"))
define lun = Character("[luna_name]", predict_function=doll_prediction("luna"))
define sus = Character("[susan_name]", predict_function=doll_prediction("susan"))
define ast = Character("[astoria_name]", predict_function=doll_prediction("astoria"))
define twi = Character("Fred and George", show_side_image=Image("characters/misc/weasley_twins/base_01.webp", xalign=1.0))
define fre = Character("Fred", show_side_image=Image("characters/misc/weasley_twins/fred_01.webp", xalign=1.0))
define ger = Character("George", show_side_image=Image("characters/misc/weasley_twins/george_01.webp", xalign=1.0))

# Teachers
define sna = Character("Severus Snape")
define ton = Character("[tonks_name]", predict_function=doll_prediction("tonks"))
define spo = Character("Professor Sprout")
define hoo = Character("Madam Hooch")

# Side characters
define hat = Character("Sorting Hat", show_side_image=Image("characters/misc/hat.webp", xalign=1.0))
define helf = Character("House-Elf", show_side_image=Image("characters/misc/elf.webp", xalign=0.95))
define malf = Character("Malfoy")
define cra = Character("Crabbe")
define goy = Character("Goyle")
define maf = Character("Madam Mafkin", show_side_image=Image("characters/misc/mafkin.webp", xalign=1.0))
define myr = Character("Moaning Myrtle")

# Non-important characters
define fem = Character("Female Student")
define femv = Character("Female Voice")
define mal = Character("Male Student")
define mal2 = Character("Another Male Student")
define sly1 = Character("Slytherin student")
define sly2 = Character("Another Slytherin student")
define qcr = Character("Quidditch Crowd")

# Special
define nar = Character("Narrator", show_side_image=Image("characters/misc/narrator.webp"))
define anon = Character("???")

# Dumbledore
define dum1 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_1.webp"))
define dum2 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_2.webp"))
define dum3 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_3.webp"))
define dum4 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_4.webp"))
define dum5 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_5.webp"))

# Santa
define san1 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_1.webp"))
define san2 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_2.webp"))
define san3 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_3.webp"))
define san4 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_4.webp"))
define san5 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_5.webp"))
define san6 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_6.webp"))
define san7 = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/santa_7.webp"))
