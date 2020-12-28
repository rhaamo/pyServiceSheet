from django.db import models
import uuid
from controllers.categories.models import Category
from controllers.manufacturers.models import Manufacturer


class Item(models.Model):
    # Internal fields
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    # Public fields
    model = models.CharField(max_length=255)
    country_of_origin = models.CharField(verbose_name="Country of Origin", max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField(unique=False, blank=True, help_text="Markdown is supported.")
    state = models.CharField(max_length=255)

    serial_number = models.CharField(max_length=255, blank=True, null=True)
    plate_infos = models.TextField(blank=True, null=True, help_text="Markdown is supported.")

    category = models.ForeignKey(Category, verbose_name="Category", blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    size = models.CharField(max_length=255, blank=True, null=True)

    # gallery attachments
    # files attachments
    # related links
    # weights FK o2m of (int, str, str)
    # powers FK o2m of (str)
    # related parts FK Item

    # Private fields
    acquired = models.DateTimeField(blank=True, null=True)
    private = models.BooleanField(default=False)
    buy_price = models.FloatField(blank=True, null=True, default=None)
    can_be_sold = models.BooleanField(default=False)
    private_note = models.TextField(unique=False, blank=True)

    class Meta(object):
        ordering = ("model",)
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        return self.model


class ItemWeight(models.Model):
    item = models.ForeignKey(Item, related_name="item_weights", blank=False, null=False, on_delete=models.CASCADE)

    weight = models.FloatField()
    unit = models.CharField(max_length=15)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.weight}{self.unit}: {self.notes}"

    class Meta(object):
        ordering = ("weight",)
