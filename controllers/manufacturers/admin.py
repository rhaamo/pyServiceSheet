from django.contrib import admin
from controllers.admin import CommonAdmin
from .models import Manufacturer


class ManufacturerAdmin(CommonAdmin):
    list_display = ("name", "notes")
    search_fields = ("name",)


admin.site.register(Manufacturer, ManufacturerAdmin)
