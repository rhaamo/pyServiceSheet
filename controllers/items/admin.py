from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Item, ItemLinks, ItemPicture, ItemPower, ItemRelated, ItemWeight, ItemWork, ItemFile
from baton.admin import DropdownFilter
from mptt.admin import TreeRelatedFieldListFilter
from imagekit.admin import AdminThumbnail
from django.forms import Textarea, TextInput
from django.db import models


class WeightsInline(admin.TabularInline):
    model = ItemWeight
    extra = 1
    verbose_name = "Weight"
    verbose_name_plural = "Weights"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 50})},
    }


class PowersInline(admin.TabularInline):
    model = ItemPower
    extra = 1
    verbose_name = "Power mode"
    verbose_name_plural = "Power modes"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class WorksInline(admin.StackedInline):
    model = ItemWork
    extra = 1
    verbose_name = "Work log"
    verbose_name_plural = "Work logs"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 100})},
        models.TextField: {"widget": Textarea(attrs={"rows": 15, "cols": 100})},
    }
    readonly_fields = ["updated_at"]
    fields = ["summary", "created_at", "content"]


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
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }


class ItemPicturesInline(admin.TabularInline):
    model = ItemPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class ItemFilesInline(admin.TabularInline):
    model = ItemFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class ItemAdmin(CommonAdmin):
    list_display = (
        "model",
        "manufacturer",
        "country_of_origin",
        "short_description",
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
    autocomplete_fields = ("manufacturer",)

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
    }

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
                    "short_description",
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
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 100})},
        models.TextField: {"widget": Textarea(attrs={"rows": 15, "cols": 100})},
    }


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

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class FilesAdmin(CommonAdmin):
    list_display = (
        "id",
        "file",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("item__model", DropdownFilter),
    ]
    autocomplete_fields = ("item",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemWork, WorkAdmin)
admin.site.register(ItemPicture, PicturesAdmin)
admin.site.register(ItemFile, FilesAdmin)
