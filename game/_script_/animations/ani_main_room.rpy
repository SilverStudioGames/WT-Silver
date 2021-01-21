

### Room Animations###
#(interactions can be found in ani_genie.rpy)


### Fireplace ###
image fireplace_fire: #Fireplace fire.
    "images/rooms/_objects_/fireplace/fireplace_fire_01.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_02.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_03.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_04.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_05.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_06.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_07.webp"
    pause.1
    "images/rooms/_objects_/fireplace/fireplace_fire_08.webp"
    pause.1
    repeat


###Glow effect###
image glow_effect: #Candle fire.
    "images/animation/glow_effect/glow_1.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_4.webp"
    pause.2
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_4.webp"
    pause.2
    "images/animation/glow_effect/glow_3.webp"
    pause.1
    "images/animation/glow_effect/glow_2.webp"
    pause.1
    "images/animation/glow_effect/glow_1.webp"
    pause.1
    repeat

### Candle Fire ###
image candle_fire_01: #Candle fire.
    "images/rooms/_objects_/candles/fire_01.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_02.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_03.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_04.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_05.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_06.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_07.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_08.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_09.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_10.webp"
    pause.1
    repeat

image candle_fire_02: #Candle fire.
    "images/rooms/_objects_/candles/fire_01.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_04.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_03.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_02.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_08.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_06.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_07.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_05.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_10.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_09.webp"
    pause.1
    repeat


### Phoenix ###
image phoenix_idle:
    zoom 0.5

    "images/rooms/_objects_/phoenix/phoenix_01.webp"
    pause 2
    "images/rooms/_objects_/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_03.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_01.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_03.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_02.webp"
    pause.15
    "images/rooms/_objects_/phoenix/phoenix_01.webp"
    pause 10
    repeat

image phoenix_hover:
    zoom 0.5

    "images/rooms/_objects_/phoenix/phoenix_hover.webp"

image phoenix_feather:
    zoom 0.5
    pause 10
    alpha 1.0
    "images/rooms/_objects_/phoenix/feather_ani/pho_01.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_02.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_03.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_04.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_05.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_06.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_07.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_08.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_09.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_10.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_11.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_12.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_13.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_14.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_15.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_16.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_17.webp"
    pause.15
    "images/rooms/_objects_/phoenix/feather_ani/pho_18.webp"
    pause 10
    linear .5 alpha 0.0
    repeat

# Door
image door_idle:
    zoom 0.5

    "images/rooms/_objects_/doors/door_idle.webp"

image door_hover:
    zoom 0.5

    "images/rooms/_objects_/doors/door_hover.webp"

image door_idle_night:
    zoom 0.5

    "images/rooms/_objects_/doors/door_idle_night.webp"

image door_hover_night:
    zoom 0.5

    "images/rooms/_objects_/doors/door_hover_night.webp"

# Fireplace
image fireplace_idle:
    zoom 0.5

    "images/rooms/_objects_/fireplace/fireplace_idle.webp"

# Fireplace
image fireplace_idle_shadow:
    zoom 0.5

    "images/rooms/_objects_/fireplace/fireplace_w_shadow.webp"

image fireplace_hover:
    zoom 0.5

    "images/rooms/_objects_/fireplace/fireplace_hover.webp"

### Owl Post ###
image owl_idle:
    zoom 0.5

    "images/rooms/_objects_/mail/owl_idle_01.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_02.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_03.webp"
    pause.15
    "images/rooms/_objects_/mail/owl_idle_02.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_idle_01.webp"
    pause 7
    repeat

image owl_letter:
    zoom 0.5

    "images/rooms/_objects_/mail/owl_01.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_02.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_03.webp"
    pause.15
    "images/rooms/_objects_/mail/owl_02.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_01.webp"
    pause 7
    repeat

image owl_letter_hover:
    zoom 0.5

    "images/rooms/_objects_/mail/owl_hover.webp"


#Black owl
image owl_idle_black:
    zoom 0.5

    "images/rooms/_objects_/mail/owl_idle_black.webp"

image owl_letter_black:
    zoom 0.5

    "images/rooms/_objects_/mail/owl_01_black.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_02_black.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_03_black.webp"
    pause.15
    "images/rooms/_objects_/mail/owl_02_black.webp"
    pause.1
    "images/rooms/_objects_/mail/owl_01_black.webp"
    pause 7
    repeat

image owl_letter_hover_black:
    zoom 0.5
    "images/rooms/_objects_/mail/owl_hover_black.webp"

image cupboard_idle:
    zoom 0.5
    "images/rooms/_objects_/cupboard/cupboard_w_shadow.webp"

image main_room_idle_day:
    zoom 0.5
    "images/rooms/_bg_/main_room_day.webp"

image main_room_idle_night:
    zoom 0.5
    "images/rooms/_bg_/main_room_night.webp"

image candle_left:
    zoom 0.5

    "images/rooms/_objects_/candles/candleM.webp"

image candle_right:
    zoom 0.5

    "images/rooms/_objects_/candles/candle.webp"

image candle_fire: #Candle fire.
    "images/rooms/_objects_/candles/fire_01.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_04.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_03.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_02.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_08.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_06.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_07.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_05.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_10.webp"
    pause.1
    "images/rooms/_objects_/candles/fire_09.webp"
    pause.1
    repeat
