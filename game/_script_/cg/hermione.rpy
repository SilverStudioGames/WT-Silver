screen hercg():
    zorder 16
    
    add her_cg_base
    add her_cg_genie        xpos her_cg_xpos_abs ypos her_cg_ypos_abs   xzoom her_cg_zoom
    add her_cg_body         xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_mouth        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eyebrow      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eyewhite     xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_pupil        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_eye          xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_cheeks       xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_tears        xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_1      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_2      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_extra_3      xpos (her_cg_xpos_abs+her_cg_xpos) ypos (her_cg_ypos_abs+her_cg_ypos)   xzoom her_cg_zoom
    add her_cg_overlay      # xpos her_cg_xpos_abs ypos her_cg_ypos_abs   xzoom her_cg_zoom # Overlay should cover the screen and not move with the CG.
    
init python:
    def herCG(mouth=None, eye=None, eyebrow=None, pupil=None, xpos=None, ypos=None, cheeks=None, tears=None, extra_1=None, extra_2=None, extra_3=None, pos=None, overlay=None, body=None):
        global her_cg_body, her_cg_overlay, her_cg_hair, her_cg_cheeks, her_cg_mouth, her_cg_eyewhite, her_cg_eyewear, her_cg_pupil, her_cg_eye, her_cg_eyebrow, her_cg_eyewear, her_cg_tears, her_cg_hairtop, her_cg_extra_1, her_cg_extra_2, her_cg_extra_3, her_cg_xpos, her_cg_ypos, her_cg_dick

        ###HIDE OLD SCREEN
        renpy.hide_screen("hercg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))

        her_cg_eyewhite     = her_cg_path+"eye_white.png"

        if body:
            her_cg_body     = her_cg_path+"body_base.png"
        if cheeks:
            her_cg_cheeks   = her_cg_path+"c_"+str(cheeks)+".png"
        if mouth:
            her_cg_mouth    = her_cg_path+"m_"+str(mouth)+".png"
        if eye:
            her_cg_eye      = her_cg_path+"eye_"+str(eye)+".png"
        if eyebrow:
            her_cg_eyebrow  = her_cg_path+"eb_"+str(eyebrow)+".png"
        if pupil:
            her_cg_pupil    = her_cg_path+"pup_"+str(pupil)+".png"
        if tears:
            her_cg_tears    = her_cg_path+str(tears)+".png"
        if extra_1:
            her_cg_extra_1  = her_cg_path+str(extra_1)+".png"
        if extra_2:
            her_cg_extra_2  = her_cg_path+str(extra_2)+".png"
        if extra_3:
            her_cg_extra_3  = her_cg_path+str(extra_3)+".png"
        if xpos:
            her_cg_xpos     = xpos
        if ypos:
            her_cg_ypos     = ypos
        if overlay:
            her_cg_overlay  = her_cg_path+str(overlay)+".png"


        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("hercg")
        renpy.with_statement(Dissolve(0.1))
