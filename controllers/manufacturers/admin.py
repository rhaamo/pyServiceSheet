from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Manufacturer
from django.forms import Textarea, TextInput
from django.db import models


class ManufacturerAdmin(CommonAdmin):
    list_display = ("name", "notes")
    search_fields = ("name",)
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 100})},
        models.TextField: {"widget": Textarea(attrs={"rows": 15, "cols": 100})},
    }


admin.site.register(Manufacturer, ManufacturerAdmin)
