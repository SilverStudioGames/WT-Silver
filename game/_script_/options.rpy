
# Preferences
# https://www.renpy.org/doc/html/preferences.html

# Note: Only use default keyword for renpy preferences. Use settings.default for custom ones.
default preferences.text_cps = 40
default preferences.afm_time = 15

init python:
    settings.default('theme', 'auto') # can be 'dark', 'light', or 'auto'
    settings.default('text_color_day', '#402313ff')
    settings.default('text_color_night', '#341c0fff')
    settings.default('text_outline', '#00000000')
    settings.default("autosave", False)

default persistent.autosave = False
default persistent.save_confirm_delete = True
default persistent.text_color_day = '#402313'

default preferences.savedelwarn = True # gui
default preferences.customcursor = False # gui
default preferences.autosave = False # gui?
default preferences.tooltip = True # gui
default preferences.text_color_day = "#402313" # gui
default preferences.text_color_night = "#341c0f" # gui
default preferences.text_outline = "#00000000" # gui
default preferences.nightmode = False # gui
default preferences.tutorials = True # gui

# Configuration
# https://www.renpy.org/doc/html/config.html

# Pre-Release related flags and variables
define is_release = False
define version_stage = "" if is_release else "development"
define config.autoreload = False
define config.debug = not is_release
define config.developer = "auto"

# Game version and naming
define config.version = "1.40"
define compatible_version = 1.40
define title_version = config.version if len(config.version) < 5 else (config.version[:4] + "." + config.version[4:6])
define config.name = "WT Silver" if is_release else "WT Silver {}".format(version_stage)

# Application window settings
define config.window_title = "Witch Trainer: Silver ({} {})".format(title_version, version_stage)
define config.window_icon = "gui/window_icon.png"
define config.screen_width = 1080
define config.screen_height = 600
define config.save_physical_size = True
define config.window_icon = "interface/icon.webp"

# User interface settings
define config.layers = ["master", "transient", "screens", "interface", "overlay"]
define config.transparent_tile = False
define config.quit_action = Quit(True)
define config.narrator_menu = True
define config.hard_rollback_limit = 150
define config.history_length = 250
define config.mouse = None # Broken in 7.4 nightly {"default": [("interface/cursor.webp", 0, 0)]} if preferences.customcursor else None
define config.help = None

# Graphics and cache settings
define config.gl2 = True
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
define config.atl_one_frame = False

# Disable automatic image scanning
define config.automatic_images = None
define config.images_directory = None
init -1:
    define config.late_images_scan = True

# Saving and loading
define config.save_directory = "WT SILVER"
define config.has_autosave = persistent.autosave
define config.autosave_on_quit = persistent.autosave
define config.autosave_on_choice = False
define config.autosave_frequency = 100

# Sound and music
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.sound_sample_rate = 48000
define config.main_menu_music = "music/01 Prologue.mp3"

# Transitions
define config.enter_transition = f3
define config.exit_transition = f3
define config.intra_transition = d3
define config.main_game_transition = f3
define config.game_main_transition = f3
define config.end_splash_transition = dissolve
define config.end_game_transition = fade
define config.after_load_transition = fade
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
#define config.manage_gc = True
#define config.gc_thresholds = (30000, 10, 10)
#define config.idle_gc_count = 3000
#define config.gc_print_unreachable = False

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
    build.classify('**~', None)
    build.classify("**.exe", None)
    build.classify("**.psd", None)
    build.classify("**.old", None)
    build.classify('**.bak', None)
    build.classify("**.kra", None)
    build.classify("**.txt", None)
    build.classify("**.xml", None)
    build.classify('**/thumbs.db', None)
    build.classify("game/saves/**", None)
    build.classify("game/outfits/**", None)
    build.classify("game/music/not_used/**", None)
    build.classify("build/", None)
    build.classify("build-*", None)

    build.allow_integrated_gpu = True # Only affects MacOS
