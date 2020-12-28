from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Item, ItemWeight
from django_admin_listfilter_dropdown.filters import DropdownFilter
from mptt.admin import TreeRelatedFieldListFilter


class WeightsInline(admin.TabularInline):
    model = ItemWeight
    extra = 1


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
    inlines = [WeightsInline]  # gallery attachments, files attachments, related links, weights, powers, related FK items?
    list_filter = [
        ("manufacturer__name", DropdownFilter),
        ("country_of_origin", DropdownFilter),
        ("category", TreeRelatedFieldListFilter),
    ]
    autocomplete_fields = (
        "category",
        "manufacturer",
    )


admin.site.register(Item, ItemAdmin)
