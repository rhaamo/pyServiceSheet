from django.contrib import admin
from .models import Category
from controllers.admin import CommonAdmin
from mptt.admin import MPTTModelAdmin
from django.forms import TextInput
from django.db import models


class CategoryAdmin(MPTTModelAdmin, CommonAdmin):
    search_fields = ["name"]
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 50})},
    }


admin.site.register(Category, CategoryAdmin)
