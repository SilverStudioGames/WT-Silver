label splashscreen:
    scene black

    call screen splashscreen with dissolve

    $ persistent.consent = True
    return

screen splashscreen():
    tag splashscreen
    style_prefix "splash"

    default consent = persistent.consent or False

    add "gui/splash/legal.webp" at splashcreen_zoomin

    vbox:
        align (0.5, 0.9)
        text "The game contains strong language, nudity, explicit scenes, drinkin', smokin', bangin', use of drugs, and just about everything your mother ever told you not to do."
        text "{color=#ff0000}{b}NOT SUITABLE FOR CHILDREN{/u}{/color}!" size 22

    timer 7.0 action Return()

    if consent:
        use invisible_button(action=Return())

style splash_text:
    color "#ffffff"
    outlines [(2, "#000", 1, 1)]
    xsize 580
    xalign 0.5

transform splashcreen_zoomin:
    subpixel True
    transform_anchor True
    zoom 0.5
    align (0.5, 0.5)
    linear 100.0 zoom 1.0
