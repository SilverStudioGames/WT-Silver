################################################
##                Preferences                 ##
################################################

default preferences.text_cps = 40
default preferences.afm_time = 15
default preferences.savedelwarn = True
default preferences.customcursor = False
default preferences.autosave = False
default preferences.tooltip = True
default preferences.text_color_day = "#402313"
default preferences.text_color_night = "#341c0f"
default preferences.text_outline = "#00000000"
default preferences.nightmode = False
default preferences.use_drawable_resolution = False if renpy.android else True
default preferences.tutorials = True

# DO NOT MODIFY ANYTHING BELOW THIS LINE IF YOU DON'T KNOW WHAT YOU'RE DOING.

################################################
##          Ren'py Configuration              ##
##      For information please refer to:      ##
## https://www.renpy.org/doc/html/config.html ##
################################################

# Pre-Release related flags and variables
define is_release = False
define _experimental = "" if is_release else " Preview"
define config.autoreload = False
define config.debug = not is_release
define config.developer = "auto"

# Game version and naming
define config.version = "1.393"
define compatible_version = 1.39
define title_version = config.version if len(config.version) < 5 else (config.version[:4] + "." + config.version[4:6])
define config.name = "WT Silver{}".format(_experimental)
define config.window_title = "Witch Trainer (Silver) {}{}".format(title_version, _experimental)

# Application Window settings
define config.screen_width = 1080
define config.screen_height = 600
define config.save_physical_size = True
define config.window_icon = "interface/icon.webp"

# User interface settings
define config.layers = ["master", "transient", "screens", "interface", "overlay"]
define config.transparent_tile = False

# Graphics and cache settings
define config.gl_enable = True
define config.gl_resize = True
define config.gl_clear_color = "#000"
define config.hw_video = True
define config.nearest_neighbor = False
define config.cache_surfaces = False
define config.image_cache_size_mb = 1024
define config.load_before_transition = True
define config.imagemap_cache = True
define config.optimize_texture_bounds = True
define config.debug_image_cache = False
define config.use_drawable_resolution = preferences.use_drawable_resolution
define config.drawable_resolution_text = preferences.use_drawable_resolution

# Disable automatic image scanning
define config.automatic_images = None
define config.images_directory = None
init -1:
    define config.late_images_scan = True

# Saving and Loading
define config.save_directory = "WT SILVER"
define config.has_autosave = preferences.autosave
define config.autosave_on_quit = preferences.autosave
define config.autosave_on_choice = False
define config.autosave_frequency = 100

# Sound and music settings
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.sound_sample_rate = 48000
define config.main_menu_music = "music/01 Prologue.mp3"
#define config.enter_sound = "click.wav"
#define config.exit_sound = "click.wav"
#define config.sample_sound = "click.wav"

# General
define config.quit_action = Quit(True)
define config.narrator_menu = True
define config.hard_rollback_limit = 150
define config.mouse = {"default": [("interface/cursor.webp", 0, 0)]} if preferences.customcursor else None

# Help (Not implemented)
define config.help = None

# Transitions
define config.enter_transition = CropMove(0.12, "irisout")
define config.exit_transition = CropMove(0.12, "irisin")
define config.intra_transition = None
define config.main_game_transition = None
define config.game_main_transition = fade
define config.end_splash_transition = dissolve
define config.end_game_transition = fade
define config.after_load_transition = CropMove(0.5, "irisout")
define config.window_show_transition = d3
define config.window_hide_transition = d3
define config.adv_nvl_transition = d3
define config.nvl_adv_transition = d3
define config.enter_yesno_transition = None
define config.exit_yesno_transition = None
define config.enter_replay_transition = None
define config.exit_replay_transition = None
define config.say_attribute_transition = d3

# Garbage Collector
define config.manage_gc = True
define config.gc_thresholds = (30000, 10, 10)
define config.idle_gc_count = 3000
define config.gc_print_unreachable = False

################################################
##           Build configuration              ##
##      For information please refer to:      ##
## https://www.renpy.org/doc/html/build.html  ##
################################################

init python:
    build.directory_name = "WT_Silver_{}".format(title_version)
    build.executable_name = "WT Silver"
    build.include_update = False # If True, include update information into packages (allows the updater to run)
    build.exclude_empty_directories = False

    build.classify("game/mods/DISABLEMODS.txt", "all")
    build.classify("game/images.whitespace", "all")
    build.classify("**.exe", None)
    build.classify("**.psd", None)
    build.classify("**.psd~", None)
    build.classify("**.old", None)
    build.classify('**.bak', None)
    build.classify("**.kra", None)
    build.classify("**.kra~", None)
    build.classify("**.txt", None)
    build.classify("**.xml", None)
    build.classify('**/thumbs.db', None)
    build.classify("game/saves/**", None)
    build.classify("game/outfits/**", None)
    build.classify("game/music/not_used/**", None)
    build.classify("build/", None)
    build.classify("build-*", None)

    build.allow_integrated_gpu = True # MacOS support Only!
