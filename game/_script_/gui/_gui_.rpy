#
# GUI configuration
#

init offset = -2

init python in gui:
    import store
    from store import settings, ScreenshotImage

    init(1080, 600)

    def is_dark():
        theme = settings.get('theme')
        if theme != 'auto':
            return theme != 'light'
        try:
            return store._menu or store.interface_color == 'gray' or not store.game.daytime
        except:
            return store._menu

    def is_light():
        return not is_dark()

    def theme(name=None):
        """
        Returns a style name or prefix that accounts for dark/light theme.
        The returned form is '{theme}_{name}', so styles can fall back on parent styles.
        """
        theme = 'dark' if is_dark() else 'light'
        return '{}_{}'.format(theme, name) if name else theme

    def format(template):
        """
        Formats a string using the current theme.
        Note: Theme name follows folder naming, so 'gray/gold' instead of 'dark/light'.
        """
        return template.format('gray' if is_dark() else 'gold')

    def rebuild_styles():
        """
        Evaluates and rebuilds styles.
        """
        for s in renpy.translation.deferred_styles:
            s.apply()

        renpy.style.rebuild()

    def menu_item(label, value, **kwargs):
        """
        Creates a menu item with arguments.
        """
        location = renpy.game.context().current
        action = renpy.ui.ChoiceReturn(label, value, location, kwargs=kwargs)
        return (label, action)

    def in_context(label, *args, **kwargs):
        """
        Calls label in a new context with captured background.
        """
        bg = ScreenshotImage.capture()
        renpy.call_in_new_context("gui_init_context", bg, label, *args, **kwargs)

label gui_init_context(bg, label, *args , **kwargs):
    $ renpy.show('screenshot', what=bg, at_list=[Transform(size=(config.screen_width, config.screen_height))])
    $ renpy.call(label, *args, **kwargs)
    return

# Colors
define gui.text_color = '#fff'
define gui.interface_text_color = '#fff'

# An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#ebc275' # '#ee7700' # '#cc6600'

# The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = Color('#000', alpha=0.5)

# The small color is used for small text, which needs to be brighter/darker to achieve the same effect.
define gui.idle_small_color = Color('#000', alpha=0.5)

# The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#000'

# The color used for a text button when it is selected but not focused.
define gui.selected_color = '#fff'

# The color used for a text button when it cannot be selected.
define gui.insensitive_color = Color('#000', alpha=0.3)

# Colors used for the portions of bars that are not filled in.
define gui.muted_color = '#88888844' # '#512800'
define gui.hover_muted_color = '#ee770044' # '#7a3d00'

# Fonts
define gui.text_font = 'gui/CreativeBlockRegular.ttf'
define gui.bold_font = 'gui/CreativeBlockBold.ttf'
define gui.glyph_font = 'DejaVuSans.ttf'

# Main and game menus
define gui.main_menu_background = 'main_menu'
define gui.game_menu_background = 'game_menu'

# Save slot size
define gui.slot_width = 350
define gui.slot_height = 50

define gui.page_button_borders = Borders(9, 4, 9, 4)

# Menu navigation
define gui.navigation_padding = 34
define gui.navigation_spacing = 4

# Save thumbnail size
define config.thumbnail_width = 94
define config.thumbnail_height = 50

# Save slots table
define gui.file_slot_cols = 2
define gui.file_slot_rows = 6

# Spacing
define gui.pref_spacing = 9
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 9

# Sliders and Bars
define gui.bar_size = 20
define gui.scrollbar_size = 12
define gui.slider_size = 20
define gui.thumb_size = 12

define gui.slider_tile = False
define gui.slider_borders = Borders(10, 10, 10, 10)

define gui.unscrollable = 'hide'
