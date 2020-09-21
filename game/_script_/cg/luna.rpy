screen luncg():
    zorder 16

    add lun_cg_base
    add lun_cg_body         xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_hair         xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_cheeks       xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_mouth        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eyewhite     xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_pupil        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eye          xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_eyebrow      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_tears        xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    if luna_wear_glasses:
        add lun_cg_eyewear  xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_hairtop      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_1      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_2      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_extra_3      xpos (lun_cg_xpos_abs+lun_cg_xpos) ypos (lun_cg_ypos_abs+lun_cg_ypos)   xzoom lun_cg_zoom
    add lun_cg_overlay      # xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom # Overlay should cover the screen and not move with the CG.
    add lun_cg_dick         xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom
    add lun_cg_genie        xpos lun_cg_xpos_abs ypos lun_cg_ypos_abs   xzoom lun_cg_zoom

init python:###THANKS TO CLEANZO FOR WRITING THIS CODE
    def lunCG(mouth=None, eye=None, eyebrow=None, pupil=None, xpos=None, ypos=None, cheeks=None, tears=None, extra_1=None, extra_2=None, extra_3=None, pos=None, overlay=None, body=None):
        global lun_cg_body, lun_cg_overlay, lun_cg_hair, lun_cg_cheeks, lun_cg_mouth, lun_cg_eyewhite, lun_cg_eyewear, lun_cg_pupil, lun_cg_eye, lun_cg_eyebrow, lun_cg_eyewear, lun_cg_tears, lun_cg_hairtop, lun_cg_extra_1, lun_cg_extra_2, lun_cg_extra_3, lun_cg_xpos, lun_cg_ypos, lun_cg_dick

        lun_cg_eyewhite     = lun_cg_path+"eye_white.webp"
        lun_cg_eyewear      = lun_cg_path+"glasses.webp"
        lun_cg_hair         = lun_cg_path+"playful_hair.webp"
        lun_cg_hairtop      = lun_cg_path+"playful_hair_top.webp"

        if body:
            lun_cg_body     = lun_cg_path+"luna_base.webp"
        if cheeks:
            lun_cg_cheeks   = lun_cg_path+"c_"+str(cheeks)+".webp"
        if mouth:
            lun_cg_mouth    = lun_cg_path+"m_"+str(mouth)+".webp"
        if eye:
            lun_cg_eye      = lun_cg_path+"eye_"+str(eye)+".webp"
        if eyebrow:
            lun_cg_eyebrow  = lun_cg_path+"eb_"+str(eyebrow)+".webp"
        if pupil:
            lun_cg_pupil    = lun_cg_path+"pup_"+str(pupil)+".webp"
        if tears:
            lun_cg_tears    = lun_cg_path+str(tears)+".webp"
        if extra_1:
            lun_cg_extra_1  = lun_cg_path+str(extra_1)+".webp"
        if extra_2:
            lun_cg_extra_2  = lun_cg_path+str(extra_2)+".webp"
        if extra_3:
            lun_cg_extra_3  = lun_cg_path+str(extra_3)+".webp"
        if xpos:
            lun_cg_xpos     = xpos
        if ypos:
            lun_cg_ypos     = ypos
        if overlay:
            lun_cg_overlay  = lun_cg_path+str(overlay)+".webp"

        if pos != None:
            lun_cg_xpos = lun_loop_xpos[pos]
            lun_cg_ypos = lun_loop_ypos[pos]
            lun_cg_dick = lun_cg_path+"dick_"+str(pos)+".webp"
