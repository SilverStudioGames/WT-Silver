
# Custom settings store

init offset = -10

default persistent.custom_settings = {}
default persistent.custom_settings_default = {}

init python in settings:
    from store import persistent, Action, DictEquality

    not_set = object()

    prefs = persistent.custom_settings
    defaults = persistent.custom_settings_default

    def default(name, default):
        value = defaults.get(name, not_set)
        if value == not_set or value != default:
            defaults[name] = default
            set(name, default)

    def get(name):
        return prefs[name]

    def set(name, value):
        prefs[name] = value

    def toggle(name, a, b):
        value = prefs.get(name, not_set)
        prefs[name] = a if value != a else b

    def reset(name):
        default = defaults.get(name, not_set)
        if default != not_set:
            prefs[name] = default

    class Set(Action, DictEquality):
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __call__(self):
            set(self.name, self.value)

        def get_selected(self):
            return prefs.get(self.name, not_set) == self.value

    class Reset(Action, DictEquality):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            reset(self.name)

        def get_sensitive(self):
            return prefs.get(self.name, not_set) != defaults.get(self.name, not_set)

    class Toggle(Action, DictEquality):
        def __init__(self, name, true_value=True, false_value=False):
            self.name = name
            self.true_value = true_value
            self.false_value = false_value

        def __call__(self):
            toggle(self.name, self.true_value, self.false_value)

        def get_selected(self):
            return prefs[self.name] == self.true_value
