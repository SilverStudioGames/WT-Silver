# Sprite blinking
image spr_hermione blink = sprite_blink("characters/hermione/face/eyes/closed.webp")
image spr_hermione blink masturbate = sprite_blink("characters/hermione/face/eyes/closed.webp")

# Hermione Solo Animations
image ch_hem blink:
    random_blink("characters/hermione/chibis/walk/h_walk_a_06.webp", "characters/hermione/chibis/walk/h_walk_a_01.webp")

image ch_hem drink_potion:
    xoffset -30
    "characters/hermione/chibis/potion/drink_1.webp"
    pause 1
    "characters/hermione/chibis/potion/drink_2.webp"
    pause 1
    "characters/hermione/chibis/potion/drink_3.webp"
    pause 2
    "characters/hermione/chibis/potion/drink_4.webp"
    pause 1.5
    repeat

image ch_hem walk:    #shirt 00
    "characters/hermione/chibis/walk/h_walk_a_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_a_04.webp"
    pause.08
    repeat

image ch_hem blink_a:
    random_blink("characters/hermione/chibis/walk/h_walk_a_06.webp", "characters/hermione/chibis/walk/h_walk_a_01.webp")

image ch_hem walk_b:    #shirt 00.1
    "characters/hermione/chibis/walk/h_walk_b_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_b_04.webp"
    pause.08
    repeat

image ch_hem blink_b:
    random_blink("characters/hermione/chibis/walk/h_walk_b_06.webp", "characters/hermione/chibis/walk/h_walk_b_01.webp")

image ch_hem walk_c:    #shirt 00.2
    "characters/hermione/chibis/walk/h_walk_c_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_c_04.webp"
    pause.08
    repeat

image ch_hem blink_c:
    random_blink("characters/hermione/chibis/walk/h_walk_c_06.webp", "characters/hermione/chibis/walk/h_walk_c_01.webp")

image ch_hem walk_d:    #shirt 01
    "characters/hermione/chibis/walk/h_walk_d_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_d_04.webp"
    pause.08
    repeat

image ch_hem blink_d:
    random_blink("characters/hermione/chibis/walk/h_walk_d_06.webp", "characters/hermione/chibis/walk/h_walk_d_01.webp")

image ch_hem walk_e:    #shirt 02
    "characters/hermione/chibis/walk/h_walk_e_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_e_04.webp"
    pause.08
    repeat

image ch_hem blink_e:
    random_blink("characters/hermione/chibis/walk/h_walk_e_06.webp", "characters/hermione/chibis/walk/h_walk_e_01.webp")

image ch_hem walk_f:    #shirt 03
    "characters/hermione/chibis/walk/h_walk_f_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_f_04.webp"
    pause.08
    repeat

image ch_hem blink_f:
    random_blink("characters/hermione/chibis/walk/h_walk_f_06.webp", "characters/hermione/chibis/walk/h_walk_f_01.webp")

image ch_hem walk_g:    #shirt 04
    "characters/hermione/chibis/walk/h_walk_g_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_g_04.webp"
    pause.08
    repeat

image ch_hem blink_g:
    random_blink("characters/hermione/chibis/walk/h_walk_g_06.webp", "characters/hermione/chibis/walk/h_walk_g_01.webp")

image ch_hem walk_h:    #shirt 05
    "characters/hermione/chibis/walk/h_walk_h_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_h_04.webp"
    pause.08
    repeat

image ch_hem blink_h:
    random_blink("characters/hermione/chibis/walk/h_walk_h_06.webp", "characters/hermione/chibis/walk/h_walk_h_01.webp")

image ch_hem walk_n:    #no shirt
    "characters/hermione/chibis/walk/h_walk_n_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_n_04.webp"
    pause.08
    repeat

image ch_hem blink_n:
    random_blink("characters/hermione/chibis/walk/h_walk_n_06.webp", "characters/hermione/chibis/walk/h_walk_n_01.webp")

image ch_hem walk_robe: #hermione walking in robe
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_04.webp"
    pause.08
    repeat

image ch_hem blink_robe:
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause 2
    "characters/hermione/chibis/walk/h_walk_robe_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause 5
    "characters/hermione/chibis/walk/h_walk_robe_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_01.webp"
    pause 3
    repeat

image ch_hem walk_robe_n: #hermione walking in robe naked
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_03.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_02.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_04.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_05.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_04.webp"
    pause.08
    repeat

image ch_hem blink_robe_n:
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause 2
    "characters/hermione/chibis/walk/h_walk_robe_n_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause 5
    "characters/hermione/chibis/walk/h_walk_robe_n_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_01_blink.webp"
    pause.08
    "characters/hermione/chibis/walk/h_walk_robe_n_01.webp"
    pause 3
    repeat

image ch_hem run:
    "characters/hermione/chibis/run/h_run_01.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_02.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_03.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_02.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_01.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_04.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_05.webp"
    pause.07
    "characters/hermione/chibis/run/h_run_04.webp"
    pause.07
    repeat

image ch_hem fly_a:
    "characters/hermione/chibis/broom/shime13a.webp"
    pause.1
    "characters/hermione/chibis/broom/shime13b.webp"
    pause.1
    "characters/hermione/chibis/broom/shime13c.webp"
    pause.1
    "characters/hermione/chibis/broom/shime13d.webp"
    pause.2
    "characters/hermione/chibis/broom/shime13c.webp"
    pause.1
    "characters/hermione/chibis/broom/shime13b.webp"
    pause.2
    "characters/hermione/chibis/broom/shime13c.webp"
    pause.1
    "characters/hermione/chibis/broom/shime13b.webp"
    pause.1
    repeat

image ch_hem kneel:
    "characters/hermione/chibis/kneel/1.webp"

image ch_hem kneel_pant:
    "characters/hermione/chibis/kneel/1.webp"
    pause 1
    "characters/hermione/chibis/kneel/2.webp"
    pause 1
    repeat

image ch_hem sit:
    #TODO Make chibi blink
    #TODO Draw and add clothing layers (not really a priority unless required for some event)
    # zoom 0.8 # chibi image is slightly too big?
    "characters/hermione/chibis/sitting/sit_naked_blink.webp"

image ch_hem sit_naked:
    #TODO Make chibi blink
    # zoom 0.8 # chibi image is slightly too big?
    "characters/hermione/chibis/sitting/sit_naked_blink.webp"

image ch_hem sit_naked_shocked:
    # zoom 0.8 # chibi image is slightly too big?
    "characters/hermione/chibis/sitting/sit_naked.webp"

image ch_hem hit_head:
    "characters/hermione/chibis/hit_on_head/01.webp"
    pause.1
    "characters/hermione/chibis/hit_on_head/02.webp"
    pause.1
    "characters/hermione/chibis/hit_on_head/03.webp"
    pause.1
    "characters/hermione/chibis/hit_on_head/04.webp"
    pause.1
    repeat

image ch_hem lying:
    zoom 2.1 #TODO Upscale image (maybe make it less flat as well?)
    "characters/hermione/chibis/lying/shime21.webp"

### HERMIONE DANCING ###
image clothed_dance_ani: # Fully clothed
    "characters/hermione/chibis/dance/01_dancing_01.webp"
    pause.1
    "characters/hermione/chibis/dance/01_dancing_02.webp"
    pause.1
    "characters/hermione/chibis/dance/01_dancing_03.webp"
    pause.1
    "characters/hermione/chibis/dance/01_dancing_04.webp"
    pause.1
    repeat

image no_vest_dance_ani: # No vest
    "characters/hermione/chibis/dance/02_no_vest_01.webp"
    pause.1
    "characters/hermione/chibis/dance/02_no_vest_02.webp"
    pause.1
    "characters/hermione/chibis/dance/02_no_vest_03.webp"
    pause.1
    "characters/hermione/chibis/dance/02_no_vest_04.webp"
    pause.1
    repeat

image no_skirt_dance_ani: # No skirt
    "characters/hermione/chibis/dance/04_no_skirt_01.webp"
    pause.1
    "characters/hermione/chibis/dance/04_no_skirt_02.webp"
    pause.1
    "characters/hermione/chibis/dance/04_no_skirt_03.webp"
    pause.1
    "characters/hermione/chibis/dance/04_no_skirt_04.webp"
    pause.1
    repeat

image no_shirt_dance_ani: # No shirt
    "characters/hermione/chibis/dance/03_no_shirt_01.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_02.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_03.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_04.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_05.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_06.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_07.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_08.webp"
    pause.1
    "characters/hermione/chibis/dance/03_no_shirt_09.webp"
    pause.1
    repeat

image no_shirt_no_skirt_dance_ani: # No shirt, no skirt
    "characters/hermione/chibis/dance/05_panties_01.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_02.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_03.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_04.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_05.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_06.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_07.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_08.webp"
    pause.1
    "characters/hermione/chibis/dance/05_panties_09.webp"
    pause.1
    repeat

image no_shirt_no_skirt_dance_pause:
    "characters/hermione/chibis/dance/05_panties_01.webp"

image no_panties_dance_ani: # No panties
    "characters/hermione/chibis/dance/07_dance_01.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_02.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_03.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_04.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_05.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_06.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_07.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_08.webp"
    pause.1
    "characters/hermione/chibis/dance/07_dance_09.webp"
    pause.1
    repeat

image no_panties_dance_pause:
    "characters/hermione/chibis/dance/07_dance_01.webp"

image hermione_stripper_dance:
    "characters/hermione/chibis/dance/strip_01.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_02.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_03.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_04.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_05.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_06.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_07.webp"
    pause.15
    "characters/hermione/chibis/dance/strip_08.webp"
    pause.15
    repeat

image ch_hem lift_top:
    zoom 0.92 # chibi is slightly too big
    xoffset -84
    yoffset -18

    "characters/hermione/chibis/lift_top/boing01.webp"
    pause 1
    "characters/hermione/chibis/lift_top/boing01.webp"
    pause .22
    "characters/hermione/chibis/lift_top/boing02.webp"
    pause .22
    "characters/hermione/chibis/lift_top/boing03.webp"
    pause .22
    "characters/hermione/chibis/lift_top/boing04.webp"
    pause .22
    "characters/hermione/chibis/lift_top/boing05.webp"
    pause 1
    # End with blink loop
    random_blink("characters/hermione/chibis/lift_top/boing06.webp", "characters/hermione/chibis/lift_top/boing05.webp")

image ch_hem reading:
    "characters/hermione/chibis/reading/0.webp"
    pause.15
    "characters/hermione/chibis/reading/1.webp"
    pause.15
    "characters/hermione/chibis/reading/2.webp"
    pause.15
    "characters/hermione/chibis/reading/3.webp"
    pause.15
    "characters/hermione/chibis/reading/4.webp"
    pause.15
    "characters/hermione/chibis/reading/0.webp"
    pause.5
    "characters/hermione/chibis/reading/5.webp"
    pause.5
    "characters/hermione/chibis/reading/0.webp"
    pause.15
    repeat

image ch_hem reading sleep:
    "characters/hermione/chibis/reading/0_sleep.webp"
    pause.15
    "characters/hermione/chibis/reading/1_sleep.webp"
    pause.15
    repeat

image ch_hem ribbon:
    zoom 0.5
    anchor (0.5, 1.0)

    "characters/hermione/chibis/ribbon/default.webp"
    pause 2
    "characters/hermione/chibis/ribbon/blink.webp"
    pause.08
    "characters/hermione/chibis/ribbon/default.webp"
    pause 5
    "characters/hermione/chibis/ribbon/blink.webp"
    pause.08
    "characters/hermione/chibis/ribbon/default.webp"
    pause.08
    "characters/hermione/chibis/ribbon/blink.webp"
    pause.08
    "characters/hermione/chibis/ribbon/default.webp"
    pause 3
    repeat
