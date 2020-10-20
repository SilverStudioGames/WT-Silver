
default weather = None
default full_moon = False
default moon_cycle = 7

define weather_types = ("clear", "cloudy", "overcast", "blizzard", "snow", "storm", "rain")

init python:
    def set_moon(full=None):
        """Sets the moon phase based on predefined frequency, or boolean argument."""
        global full_moon, moon_cycle

        if full is not None:
            full_moon = bool(full)
        else:
            # Full moon averages every 7 days
            if game.day % moon_cycle == 0:
                full_moon = True
                moon_cycle = renpy.random.randint(5,9)
            else:
                full_moon = False

    def set_weather(*args):
        """Sets the weather based on predefined chance, or randomly picks a weather type from the arguments."""
        global weather

        if args:
            if any((x not in weather_types for x in args)):
                raise Exception("Unsupported weather type in {}".format(args))
            weather = renpy.random.choice(args)
            return

        weather_gen = renpy.random.randint(1, 6)

        if weather_gen <= 2:
            weather = "clear"
        elif weather_gen == 3:
            weather = "cloudy"
        elif weather_gen == 4:
            weather = "overcast"
        else:
            snow_gen = renpy.random.randint(1, 3) == 1
            storm_gen = renpy.random.randint(1, 3) == 1

            if snow_gen and game.day >= 30:
                weather = "blizzard" if storm_gen else "snow"
            elif storm_gen:
                weather = "storm"
            else:
                weather = "rain"

label weather_sound:
    if weather == "blizzard":
        play weather "sounds/blizzard.ogg" fadeout 0.5 fadein 0.5 if_changed
    elif weather == "storm":
        play weather "sounds/storm.mp3" fadeout 0.5 fadein 0.5 if_changed
    elif weather == "rain":
        play weather "sounds/storm.mp3" fadeout 0.5 fadein 0.5 if_changed # TODO: Rain sound (without thunder)
    else:
        stop weather fadeout 0.5
    return

screen weather():
    zorder -1
    sensitive False

    if game.daytime:
        if weather in ("clear", "cloudy"):
            add "images/rooms/_weather_/sky.webp" pos (430, 218) anchor (0.5, 0.5)

        if weather == "cloudy":
            add "images/rooms/_weather_/cloud_small.webp" at cloud_move

        if weather in ("overcast", "blizzard", "snow", "storm", "rain"):
            add "images/rooms/_weather_/sky_overcast.webp" pos (430, 218) anchor (0.5, 0.5)

    elif full_moon:
        if weather in ("clear", "cloudy"):
            add "images/rooms/_weather_/night_sky_moon.webp" pos (430, 218) anchor (0.5, 0.5)

        if weather == "cloudy":
            add "images/rooms/_weather_/night_cloud_02.webp" at cloud_night_move_01
            add "images/rooms/_weather_/night_cloud_01.webp" at cloud_night_move_02
            add "images/rooms/_weather_/night_cloud_03.webp" at cloud_night_move_03

        if weather in ("overcast", "blizzard", "snow", "storm", "rain"):
            add "images/rooms/_weather_/night_sky_moon_overcast.webp" pos (430, 218) anchor (0.5, 0.5)

    else:
        if weather in ("clear", "cloudy"):
            add "images/rooms/_weather_/night_sky.webp" pos (430, 218) anchor (0.5, 0.5)

        if weather == "cloudy":
            add "images/rooms/_weather_/night_cloud_02.webp" at cloud_night_move_01
            add "images/rooms/_weather_/night_cloud_01.webp" at cloud_night_move_02
            add "images/rooms/_weather_/night_cloud_03.webp" at cloud_night_move_03

        if weather in ("overcast", "blizzard", "snow", "storm", "rain"):
            add "images/rooms/_weather_/night_sky_overcast.webp" pos (430, 218) anchor (0.5, 0.5)

    if weather in ("blizzard", "snow", "storm", "rain"):
        add weather pos (430, 218) anchor (0.5, 0.5)

    if weather == "storm":
        add "rain" pos (430, 218) anchor (0.5, 0.5)


transform cloud_move:
    xpos 520
    choice:
        ypos 150
    choice:
        ypos 160
    choice:
        ypos 170
    choice:
        ypos 190
    choice:
        ypos 200

    linear 15.0 xpos 237
    pause 7
    repeat

transform cloud_night_move_01:
    xpos 520
    choice:
        ypos 130
    choice:
        ypos 150
    choice:
        ypos 150
    linear 30.0 xpos 280
    pause 2
    repeat

transform cloud_night_move_02:
    xpos 520
    choice:
        ypos 150
    choice:
        ypos 170
    linear 70.0 xpos 280
    pause 2
    repeat

transform cloud_night_move_03:
    xpos 520
    ypos 160
    linear 50.0 xpos 280
    pause 2
    repeat

image rain:
    "images/rooms/_weather_/rain_01.webp"
    pause.1
    "images/rooms/_weather_/rain_02.webp"
    pause.1
    "images/rooms/_weather_/rain_03.webp"
    pause.1
    repeat

image snow:
    "images/rooms/_weather_/snow_01.webp"
    pause.07
    "images/rooms/_weather_/snow_02.webp"
    pause.07
    "images/rooms/_weather_/snow_03.webp"
    pause.07
    "images/rooms/_weather_/snow_04.webp"
    pause.07
    "images/rooms/_weather_/snow_05.webp"
    pause.07
    "images/rooms/_weather_/snow_06.webp"
    pause.07
    "images/rooms/_weather_/snow_07.webp"
    pause.07
    "images/rooms/_weather_/snow_08.webp"
    pause.07
    "images/rooms/_weather_/snow_09.webp"
    pause.07
    "images/rooms/_weather_/snow_10.webp"
    pause.07
    repeat

image blizzard:
    "images/rooms/_weather_/blizzard_01.webp"
    pause.05
    "images/rooms/_weather_/blizzard_02.webp"
    pause.05
    "images/rooms/_weather_/blizzard_03.webp"
    pause.05
    "images/rooms/_weather_/blizzard_04.webp"
    pause.05
    "images/rooms/_weather_/blizzard_05.webp"
    pause.05
    "images/rooms/_weather_/blizzard_06.webp"
    pause.05
    "images/rooms/_weather_/blizzard_07.webp"
    pause.05
    "images/rooms/_weather_/blizzard_08.webp"
    pause.05
    "images/rooms/_weather_/blizzard_09.webp"
    pause.05
    "images/rooms/_weather_/blizzard_10.webp"
    pause.05
    repeat

image storm:
    pause 20
    "images/rooms/_weather_/lightning_01.webp"
    pause.1
    "images/rooms/_weather_/lightning_02.webp"
    pause.1
    "images/rooms/_weather_/lightning_03.webp"
    pause.1
    "images/rooms/_weather_/lightning_04.webp"
    pause.1
    "images/rooms/_weather_/lightning_05.webp"
    pause.1
    "images/rooms/_weather_/lightning_06.webp"
    pause.1
    "images/rooms/_weather_/lightning_05.webp"
    pause.1
    "images/rooms/_weather_/lightning_06.webp"
    pause.1
    "images/rooms/_weather_/lightning_05.webp"
    pause 20
    repeat
