from dynamic_preferences.types import StringPreference, LongStringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry


general = Section("general")
discussion = Section("discussion")


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = "title"
    default = "Collection of dashie"
    required = True


@global_preferences_registry.register
class SiteDescription(LongStringPreference):
    section = general
    name = "about"
    default = "Collection of test equipment and various radios."
    required = True
