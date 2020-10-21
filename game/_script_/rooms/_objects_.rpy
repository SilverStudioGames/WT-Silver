default deco_list = []
default deco_overlay_list = []

default fireplace_OBJ = RoomObject(type="fireplace",
    room_image="fireplace_idle_shadow", room_image_path="",
    idle_image="fireplace_idle", idle_image_path="",
    hover_image="fireplace_hover", hover_image_path="",
    xpos=693, ypos=277)

default cupboard_top_OBJ = RoomObject(type="cupboard",
    idle_image="idle_scroll", idle_image_path="images/rooms/_objects_/cupboard/",
    hover_image="hover_scroll", hover_image_path="images/rooms/_objects_/cupboard/",
    xpos=260, ypos=280)

default cupboard_OBJ = RoomObject(type="cupboard",
    room_image="cupboard_w_shadow", room_image_path="images/rooms/_objects_/cupboard/",
    idle_image="cupboard_idle", idle_image_path="images/rooms/_objects_/cupboard/",
    hover_image="cupboard_hover", hover_image_path="images/rooms/_objects_/cupboard/",
    xpos=260, ypos=280)

default hat_OBJ = RoomObject(type="hat",
    room_image="hat_idle", room_image_path="images/rooms/_objects_/cupboard/",
    idle_image="hat_idle", idle_image_path="images/rooms/_objects_/cupboard/",
    hover_image="hat_hover", hover_image_path="images/rooms/_objects_/cupboard/",
    xpos=260, ypos=280)

default phoenix_OBJ = RoomObject(type="phoenix",
    room_image="phoenix_idle", room_image_path="",
    idle_image="phoenix_idle", idle_image_path="",
    hover_image="phoenix_hover", hover_image_path="",
    xpos=557, ypos=272)

default door_OBJ = RoomObject(type="door",
    room_image="door_idle", room_image_path="",
    idle_image="door_idle", idle_image_path="",
    hover_image="door_hover", hover_image_path="",
    xpos=898, ypos=315)

default door_night_OBJ = RoomObject(type="door",
    room_image="door_idle_night", room_image_path="",
    idle_image="door_idle_night", idle_image_path="",
    hover_image="door_hover_night", hover_image_path="",
    xpos=898, ypos=315
)

#default carpet_OBJ = RoomObject(type="carpet", room_image="", xpos=0, ypos=0)

default candle_left_OBJ = RoomObject(type="candle",
    room_image="candle", room_image_path="images/rooms/_objects_/candles/",
    xpos=350, ypos=160)

default candle_right_OBJ = RoomObject(type="candle",
    room_image="candle", room_image_path="images/rooms/_objects_/candles/",
    xpos=833, ypos=225)

default owl_OBJ = RoomObject(type="mail",
    room_image="owl_idle", room_image_path="",
    idle_image="owl_letter", idle_image_path="",
    hover_image="owl_letter_hover", hover_image_path="",
    xpos=455, ypos=289)

default package_OBJ = RoomObject(type="mail",
    room_image="package_idle", room_image_path="images/rooms/_objects_/mail/",
    idle_image="package_idle", idle_image_path="images/rooms/_objects_/mail/",
    hover_image="package_hover", hover_image_path="images/rooms/_objects_/mail/",
    xpos=402, ypos=290)

default xmas_fireplace_deco_ITEM = RoomObject(type="fireplace", image="deco/fireplace_xmas",
    room_image="fireplace_deco_xmas", room_image_path="images/rooms/_objects_/fireplace/")

# New Decorations
default poster_OBJ = RoomObject(type="poster",
    room_image="", room_image_path="images/rooms/_objects_/posters/",
    xpos=332, ypos=260)

default trophy_OBJ = RoomObject(type="trophy",
    room_image="", room_image_path="images/rooms/_objects_/trophies/",
    xpos=690, ypos=150)

# Phoenix hat
default phoenix_deco_OBJ = RoomObject(type="phoenix_deco",
    room_image="", room_image_path="images/rooms/_objects_/phoenix/",
    xpos=phoenix_OBJ.xpos, ypos=phoenix_OBJ.ypos-42)

default fireplace_deco_OBJ = RoomObject(type="fireplace_deco",
    room_image="", room_image_path="images/rooms/_objects_/fireplace/",
    xpos=fireplace_OBJ.xpos, ypos=fireplace_OBJ.ypos)

default owl_deco_OBJ = RoomObject(type="owl_deco",
    room_image="", room_image_path="images/rooms/_objects_/mail/",
    xpos=owl_OBJ.xpos, ypos=owl_OBJ.ypos)

default cupboard_deco_OBJ = RoomObject(type="cupboard_deco",
    room_image="", room_image_path="images/rooms/_objects_/cupboard/",
    xpos=cupboard_OBJ.xpos, ypos=cupboard_OBJ.ypos)
