from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Item, ItemPower, ItemWeight, ItemWork
from django_admin_listfilter_dropdown.filters import DropdownFilter
from mptt.admin import TreeRelatedFieldListFilter


class WeightsInline(admin.TabularInline):
    model = ItemWeight
    extra = 1
    verbose_name = "Weight"
    verbose_name_plural = "Weights"


class PowersInline(admin.TabularInline):
    model = ItemPower
    extra = 1
    verbose_name = "Power mode"
    verbose_name_plural = "Power modes"


class WorksInline(admin.StackedInline):
    model = ItemWork
    extra = 1
    verbose_name = "Work note"
    verbose_name_plural = "Work notes"


class ItemAdmin(CommonAdmin):
    list_display = (
        "model",
        "manufacturer",
        "country_of_origin",
        "state",
        "private",
        "can_be_sold",
    )
    search_fields = ("model", "state", "description")
    inlines = [
        WeightsInline,
        PowersInline,
        WorksInline,
    ]  # gallery attachments, files attachments, related links, related FK items?
    list_filter = [
        ("manufacturer__name", DropdownFilter),
        ("country_of_origin", DropdownFilter),
        ("category", TreeRelatedFieldListFilter),
    ]
    autocomplete_fields = (
        "category",
        "manufacturer",
    )


class WorkAdmin(CommonAdmin):
    list_display = (
        "summary",
        "content",
        "private",
    )
    search_fields = ("summary", "content")
    list_filter = [
        ("item__model", DropdownFilter),
    ]
    autocomplete_fields = ("item",)


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemWork, WorkAdmin)
