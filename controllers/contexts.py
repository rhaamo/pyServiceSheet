from controllers.categories.models import Category
from controllers.items.models import Item
from controllers import __version__
from django.db import models


def add_common_context(request):
    ctx = {
        "VERSION": __version__,
        "categories": Category.objects.all().annotate(
            items_count=models.Count("item", filter=models.Q(item__private=False))
        ),
        "uncategorized": Item.objects.filter(category__isnull=True, private=False).count(),
        "all_items": Item.objects.filter(private=False).count(),
    }
    return ctx
