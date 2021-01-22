
screen gui_tooltip(img=None, xx=335, yy=210):
    add img xpos xx ypos yy
    zorder 3

screen dumbledore(): # Dumbledore and desk
    tag dumbledore
    add "images/rooms/main_room/dum.webp" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5 zoom 0.5

screen chair_right():
    tag chair_right
    zorder 0 # Show main_room first for correct order
    add "images/rooms/main_room/chair_right.webp" xpos 793 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5
