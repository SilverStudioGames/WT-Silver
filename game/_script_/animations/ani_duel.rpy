
# Animation that shows a broken glass effect when the duel starts.
image glass:

    contains:
        "images/dueling/snape/glass/gradient.webp"

    contains:
        pause 1.3
        "images/dueling/snape/glass/01.webp"
        pause.1
        "images/dueling/snape/glass/02.webp"
        pause.1
        "images/dueling/snape/glass/03.webp"
        pause.1
        "images/dueling/snape/glass/04.webp"
        pause.1
        "images/dueling/snape/glass/05.webp"
        pause.1
        "images/dueling/snape/glass/06.webp"
        pause.1
        "images/dueling/snape/glass/07.webp"
        pause.1
        "images/dueling/snape/glass/08.webp"
        pause.1
        "images/dueling/snape/glass/09.webp"
        pause.1
        "images/dueling/snape/glass/10.webp"

    contains:
        "images/dueling/snape/glass/crack.webp"

image duel_table:
    zoom 0.5
    "images/rooms/main_room/desk_with_shadow.webp"

image smoke:
    zoom 0.5
    alpha 1.0
    "images/animation/smoke_01.webp"
    pause.1
    "images/animation/smoke_02.webp"
    pause.1
    "images/animation/smoke_03.webp"
    pause.1
    alpha 0.0
    pause.1

image teleport_ani:
    "magic/magic4.webp"
    pause.05
    "magic/magic5.webp"
    pause.1
    "magic/magic1.webp"
    pause.05
    "magic/magic2.webp"
    pause.3

image heal_ani:
    "magic/heal01.webp"
    pause.06
    "magic/heal02.webp"
    pause.06
    "magic/heal03.webp"
    pause.06
    "magic/heal04.webp"
    pause.06
    "magic/heal05.webp"
    pause.06
    "magic/heal06.webp"
    pause.06
    "magic/heal07.webp"
    pause.06
    "magic/heal08.webp"
    pause.06
    "magic/heal09.webp"
    pause.06
    "magic/heal10.webp"
    pause.06
    "magic/heal11.webp"
    pause.06
    "magic/heal12.webp"
    pause.06
    "magic/heal13.webp"
    pause.06
    "magic/heal14.webp"
    pause.06
    "magic/heal15.webp"
    pause.06
    "magic/heal16.webp"
    pause.06
    "magic/heal17.webp"
    pause.06
    "magic/heal18.webp"
    pause.06

image heal_02: # Smaller version of heal. 40% of the original size.
    "magic/heal_02/heal01.webp"
    pause.06
    "magic/heal_02/heal02.webp"
    pause.06
    "magic/heal_02/heal03.webp"
    pause.06
    "magic/heal_02/heal04.webp"
    pause.06
    "magic/heal_02/heal05.webp"
    pause.06
    "magic/heal_02/heal06.webp"
    pause.06
    "magic/heal_02/heal07.webp"
    pause.06
    "magic/heal_02/heal08.webp"
    pause.06
    "magic/heal_02/heal09.webp"
    pause.06
    "magic/heal_02/heal10.webp"
    pause.06
    "magic/heal_02/heal11.webp"
    pause.06
    "magic/heal_02/heal12.webp"
    pause.06
    "magic/heal_02/heal13.webp"
    pause.06
    "magic/heal_02/heal14.webp"
    pause.06
    "magic/heal_02/heal15.webp"
    pause.06
    "magic/heal_02/heal16.webp"
    pause.06
    "magic/heal_02/heal17.webp"
    pause.06
    "magic/heal_02/heal18.webp"
    pause.06


### GENIE SPELL ANIMATION ###
image spell_ani:
    "images/animation/spell01.webp"
    pause.1
    "images/animation/spell02.webp"
    pause.1
    "images/animation/spell03.webp"
    pause.1
    "images/animation/spell04.webp"
    pause.1
    "images/animation/spell05.webp"
    pause.1
    "images/animation/spell06.webp"
    pause.1
    "images/animation/spell07.webp"
    pause.1
    "images/animation/spell08.webp"
    pause.1
    "images/animation/spell09.webp"
    pause.1
    "images/animation/spell10.webp"
    pause.1
    "images/animation/spell11.webp"
    pause.1
    "images/animation/spell12.webp"
    pause.1
    "images/animation/spell13.webp"
    pause.1
    "images/animation/spell14.webp"
    pause.1
    "images/animation/spell15.webp"
    pause.1
    "images/animation/spell16.webp"
    pause.1
    "images/animation/spell17.webp"
    pause.1

image ch_sna duel_01:
    zoom 0.5
    "images/dueling/snape/snape_01.webp"
    pause.13
    "images/dueling/snape/snape_02.webp"
    pause.13
    "images/dueling/snape/snape_03.webp"
    pause.13
    "images/dueling/snape/snape_02.webp"
    pause.13
    repeat

image ch_gen duel_01:
    zoom 0.5
    "images/dueling/snape/gen_01.webp"
    pause.13
    "images/dueling/snape/gen_02.webp"
    pause.13
    "images/dueling/snape/gen_03.webp"
    pause.13
    "images/dueling/snape/gen_02.webp"
    pause.13
    repeat

image ch_gen guard:
    zoom 0.5
    "images/dueling/snape/guard_01.webp"
    pause.13
    "images/dueling/snape/guard_02.webp"
    pause.13
    "images/dueling/snape/guard_03.webp"
    pause.13
    "images/dueling/snape/guard_02.webp"
    pause.13
    repeat

image ch_gen barb:
    zoom 0.5
    "images/dueling/snape/barb_01.webp"
    pause.13
    "images/dueling/snape/barb_02.webp"
    pause.13
    repeat

image genie_no_magic:
    zoom 0.5
    "images/dueling/snape/no_magic.webp"

image ch_sna defend:
    zoom 0.5
    "images/dueling/snape/snape_defend_01.webp"
    pause.13
    "images/dueling/snape/snape_defend_02.webp"
    pause.13
    "images/dueling/snape/snape_defend_03.webp"
    pause.13
    "images/dueling/snape/snape_defend_02.webp"
    pause.13
    repeat

image snape_attack:
    zoom 0.5
    "images/dueling/snape/sna_attack_01.webp"
    pause.13
    "images/dueling/snape/sna_attack_02.webp"
    pause.13
    "images/dueling/snape/sna_attack_03.webp"
    pause.13
    "images/dueling/snape/sna_attack_04.webp"
    pause.08
    "images/dueling/snape/sna_attack_05.webp"
    pause.08
    "images/dueling/snape/sna_attack_06.webp"
    pause.08
    "images/dueling/snape/sna_attack_07.webp"
    pause.08
    "images/dueling/snape/sna_attack_08.webp"
    pause.08
    "images/dueling/snape/sna_attack_09.webp"
    pause.08
    "images/dueling/snape/sna_attack_10.webp"
    pause.08
    repeat

image snape_attack_guard:
    zoom 0.5
    "images/dueling/snape/sna_attack_guard_01.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_02.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_03.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_04.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_05.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_06.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_07.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_08.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_09.webp"
    pause.08
    "images/dueling/snape/sna_attack_guard_10.webp"
    pause.08
    repeat

image genie_attack:
    zoom 0.5
    "images/dueling/snape/genie_attack_01.webp"
    pause.15
    "images/dueling/snape/genie_attack_02.webp"
    pause.15
    "images/dueling/snape/genie_attack_01.webp"
    pause.15
    "images/dueling/snape/genie_attack_02.webp"
    pause.15
    "images/dueling/snape/genie_attack_01.webp"
    pause.15
    "images/dueling/snape/genie_attack_02.webp"
    pause.15
    "images/dueling/snape/genie_attack_03.webp"
    pause.15
    "images/dueling/snape/genie_attack_04.webp"
    pause.15
    "images/dueling/snape/genie_attack_05.webp"
    pause.15
    "images/dueling/snape/genie_attack_06.webp"
    pause.15
    "images/dueling/snape/genie_attack_07.webp"
    pause.15
    "images/dueling/snape/genie_attack_08.webp"
    pause.15
    "images/dueling/snape/genie_attack_09.webp"
    pause.15
    "images/dueling/snape/genie_attack_10.webp"
    pause.15
    "images/dueling/snape/genie_attack_11.webp"
    pause.15
    "images/dueling/snape/genie_attack_12.webp"
    pause.15
    "images/dueling/snape/genie_attack_13.webp"
    pause.15
    "images/dueling/snape/genie_attack_14.webp"
    pause.15
    "images/dueling/snape/genie_attack_15.webp"
    pause.15
    "images/dueling/snape/genie_attack_14.webp"
    pause.15
    "images/dueling/snape/genie_attack_15.webp"
    pause.15
    repeat

# Snape is in defense stance. Barbarian throws axes at him.
image snape_defend:
    zoom 0.5
    "images/dueling/snape/sna_block_01.webp"
    pause.15
    "images/dueling/snape/sna_block_02.webp"
    pause.15
    "images/dueling/snape/sna_block_01.webp"
    pause.15
    "images/dueling/snape/sna_block_02.webp"
    pause.15
    "images/dueling/snape/sna_block_01.webp"
    pause.15
    "images/dueling/snape/sna_block_02.webp"
    pause.15
    "images/dueling/snape/sna_block_03.webp"
    pause.15
    "images/dueling/snape/sna_block_04.webp"
    pause.15
    "images/dueling/snape/sna_block_05.webp"
    pause.15
    "images/dueling/snape/sna_block_06.webp"
    pause.15
    "images/dueling/snape/sna_block_07.webp"
    pause.15
    "images/dueling/snape/sna_block_08.webp"
    pause.15
    "images/dueling/snape/sna_block_09.webp"
    pause.15
    "images/dueling/snape/sna_block_10.webp"
    pause.15
    "images/dueling/snape/sna_block_11.webp"
    pause.15
    "images/dueling/snape/sna_block_12.webp"
    pause.15
    "images/dueling/snape/sna_block_13.webp"
    pause.15
    repeat

image snape_summon:
    zoom 0.5
    "images/dueling/snape/snape_casting_01.webp"

image snape_lost:
    zoom 0.5
    "images/dueling/snape/snape.webp"

image pentogram:
    zoom 0.5
    alpha 0.0
    linear .5 alpha 1.0
    "images/dueling/snape/pen_01.webp"
    linear .5 alpha 0.0
    repeat

image hand: #Hand appears.
    zoom 0.5
    "images/dueling/snape/hand_01.webp"
    pause.1
    "images/dueling/snape/hand_02.webp"
    pause.1
    "images/dueling/snape/hand_03.webp"
    pause.1
    "images/dueling/snape/hand_04.webp"
    pause.1
    "images/dueling/snape/hand_05.webp"
    pause.1
    "images/dueling/snape/hand_06.webp"
    pause.1
    "images/dueling/snape/hand_07.webp"
    pause.1
    "images/dueling/snape/hand_08.webp"
    pause.1
    "images/dueling/snape/hand_09.webp"
    pause.1
    "images/dueling/snape/hand_10.webp"
    pause.1
    "images/dueling/snape/hand_11.webp"
    pause.1
    "images/dueling/snape/hand_12.webp"
    pause.1
    "images/dueling/snape/hand_13.webp"
    pause.1
    "images/dueling/snape/hand_14.webp"
    pause.1
    "images/dueling/snape/hand_15.webp"
    pause.1
    "images/dueling/snape/hand_16.webp"
    pause.1
    repeat

image hand_genie: #Hand attacks Genie.
    zoom 0.5
    "images/dueling/snape/hand_genie_01.webp"
    pause.13
    "images/dueling/snape/hand_genie_02.webp"
    pause.13
    "images/dueling/snape/hand_genie_03.webp"
    pause.13
    "images/dueling/snape/hand_genie_04.webp"
    pause.13
    "images/dueling/snape/hand_genie_05.webp"
    pause.1
    "images/dueling/snape/hand_genie_06.webp"
    pause.1
    "images/dueling/snape/hand_genie_07.webp"
    pause.1
    "images/dueling/snape/hand_genie_08.webp"
    pause.1
    "images/dueling/snape/hand_genie_09.webp"
    pause.1
    "images/dueling/snape/hand_genie_10.webp"
    pause.1
    "images/dueling/snape/hand_genie_11.webp"
    pause.1
    "images/dueling/snape/hand_genie_12.webp"
    pause.1
    "images/dueling/snape/hand_genie_13.webp"
    pause.1

image hand_guard: #Hand attacks the guard.
    zoom 0.5
    "images/dueling/snape/hand_guard_01.webp"
    pause.1
    "images/dueling/snape/hand_guard_02.webp"
    pause.1
    "images/dueling/snape/hand_guard_03.webp"
    pause.1
    "images/dueling/snape/hand_guard_04.webp"
    pause.1
    "images/dueling/snape/hand_guard_05.webp"
    pause.1
    "images/dueling/snape/hand_guard_06.webp"
    pause.1
    "images/dueling/snape/hand_guard_07.webp"
    pause.1
    "images/dueling/snape/hand_guard_08.webp"
    pause.1
    "images/dueling/snape/hand_guard_09.webp"
    pause.1
    "images/dueling/snape/hand_guard_10.webp"
    pause.1
    "images/dueling/snape/hand_guard_11.webp"
    pause.1
    "images/dueling/snape/hand_guard_12.webp"
    pause.1
    "images/dueling/snape/hand_guard_13.webp"
    pause.1
    "images/dueling/snape/hand_guard_14.webp"
    pause.1
    "images/dueling/snape/hand_guard_11.webp"
    pause.1
    "images/dueling/snape/hand_guard_12.webp"
    pause.1
    "images/dueling/snape/hand_guard_13.webp"
    pause.1

image bouquet_appear:
    "images/animation/Bouquet0.webp"
    pause.1
    "images/animation/Bouquet1.webp"
    pause.1
    "images/animation/Bouquet2.webp"
    pause.1
    "images/animation/Bouquet3.webp"
    pause.1
    "images/animation/Bouquet4.webp"
    pause.8

image flower_appear:
    "images/animation/Flower0.webp"
    pause.1
    "images/animation/Flower1.webp"
    pause.1
    "images/animation/Flower2.webp"
    pause.1
    "images/animation/Flower3.webp"
    pause.1
    "images/animation/Flower4.webp"
    pause.8

# image vanish_effect_bouquet:
    # "images/animation/BouquetPaf.webp"
    # pause.1
    # "images/animation/PafAndSmoke.webp"
    # pause.1
    # "images/animation/NoPafSmoke.webp"
    # pause.1
    # "images/animation/NoPafSmokeTrans1.webp"
    # pause.1
    # "images/animation/NoPafSmokeTrans2.webp"
    # pause.1

# image vanish_effect_flower:
    # "images/animation/FlowerPaf.webp"
    # pause.1
    # "images/animation/PafAndSmoke.webp"
    # pause.1
    # "images/animation/NoPafSmoke.webp"
    # pause.1
    # "images/animation/NoPafSmokeTrans1.webp"
    # pause.1
    # "images/animation/NoPafSmokeTrans2.webp"
    # pause.1
