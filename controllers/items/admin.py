from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Item, ItemLinks, ItemPicture, ItemPower, ItemRelated, ItemWeight, ItemWork, ItemFile
from baton.admin import DropdownFilter
from mptt.admin import TreeRelatedFieldListFilter
from imagekit.admin import AdminThumbnail
from django.forms import Textarea
from django.db import models


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
    verbose_name = "Work log"
    verbose_name_plural = "Work logs"


class RelatedInline(admin.TabularInline):
    model = ItemRelated
    extra = 0
    fk_name = "item"
    verbose_name = "Item"
    verbose_name_plural = "Related items"


class URLsInline(admin.TabularInline):
    model = ItemLinks
    extra = 0
    verbose_name = "Link"
    verbose_name_plural = "Links"


class ItemPicturesInline(admin.TabularInline):
    model = ItemPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"


class ItemFilesInline(admin.TabularInline):
    model = ItemFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"


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
        RelatedInline,
        URLsInline,
        ItemPicturesInline,
        ItemFilesInline,
    ]
    list_filter = [
        ("manufacturer__name", DropdownFilter),
        ("country_of_origin", DropdownFilter),
        ("category", TreeRelatedFieldListFilter),
    ]
    autocomplete_fields = (
        "category",
        "manufacturer",
    )

    formfield_overrides = {models.TextField: {"widget": Textarea(attrs={"rows": 5, "cols": 80})}}

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    (
                        "model",
                        "country_of_origin",
                        "manufacturer",
                    ),
                    (
                        "state",
                        "serial_number",
                        "size",
                    ),
                    "description",
                    "plate_infos",
                    "category",
                    "acquired",
                    "private",
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p--fs-buy_price",
                    "baton-tab-group-inline-item_weights",
                    "baton-tab-group-inline-item_powers",
                    "baton-tab-group-inline-item_works",
                    "baton-tab-group-inline-related_items",
                    "baton-tab-group-inline-item_links",
                    "baton-tab-group-inline-item_pictures--inline-item_files",
                ),
            },
        ),
        (
            "Private fields",
            {
                "fields": ("buy_price", "can_be_sold", "private_note"),
                "classes": ("tab-fs-p",),
            },
        ),
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


class PicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("item__model", DropdownFilter),
    ]
    autocomplete_fields = ("item",)

    image_display = AdminThumbnail(image_field="file")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]


class FilesAdmin(CommonAdmin):
    list_display = (
        "file",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("item__model", DropdownFilter),
    ]
    autocomplete_fields = ("item",)


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemWork, WorkAdmin)
admin.site.register(ItemPicture, PicturesAdmin)
admin.site.register(ItemFile, FilesAdmin)
