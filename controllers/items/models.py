from django.db import models
import uuid

from controllers.categories.models import Category
from controllers.manufacturers.models import Manufacturer
from .validators import validate_picture, validate_other
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_CLASSY
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Item(models.Model):
    # Internal fields
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    # Public fields
    model = models.CharField(max_length=255)
    country_of_origin = models.CharField(verbose_name="Country of Origin", max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, on_delete=models.PROTECT)

    short_description = models.CharField(max_length=255, blank=True, null=True)

    description = MarkdownField(
        blank=True,
        rendered_field="description_rendered",
        help_text="Markdown is supported.",
        validator=VALIDATOR_CLASSY,
    )
    description_rendered = RenderedMarkdownField()

    state = models.CharField(max_length=255)

    serial_number = models.CharField(max_length=255, blank=True, null=True)

    plate_infos = MarkdownField(
        blank=True,
        null=True,
        rendered_field="plate_infos_rendered",
        help_text="Markdown is supported.",
        validator=VALIDATOR_CLASSY,
    )
    plate_infos_rendered = RenderedMarkdownField()

    category = models.ForeignKey(Category, verbose_name="Category", blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    size = models.CharField(max_length=255, blank=True, null=True)

    # Private fields
    acquired = models.DateTimeField(blank=True, null=True)
    private = models.BooleanField(default=False)
    buy_price = models.IntegerField(blank=True, null=True, default=None)
    can_be_sold = models.BooleanField(default=False)
    private_note = models.TextField(unique=False, blank=True)

    class Meta(object):
        ordering = ("model",)
        verbose_name = "item"
        verbose_name_plural = "items"

    def __str__(self):
        extras = []
        if self.manufacturer:
            extras.append(self.manufacturer.name)
        else:
            extras.append("Unknown")

        if self.country_of_origin:
            extras.append(self.country_of_origin)

        name = self.model

        if len(extras) > 0:
            name += f" ({', '.join(extras)})"

        return name


class ItemWeight(models.Model):
    item = models.ForeignKey(Item, related_name="item_weights", blank=False, null=False, on_delete=models.CASCADE)

    weight = models.FloatField()
    unit = models.CharField(max_length=15)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.weight}{self.unit}: {self.notes}"

    class Meta(object):
        ordering = ("weight",)


class ItemPower(models.Model):
    item = models.ForeignKey(Item, related_name="item_powers", blank=False, null=False, on_delete=models.CASCADE)

    mode = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.mode

    class Meta(object):
        ordering = ("mode",)


class ItemWork(models.Model):
    item = models.ForeignKey(Item, related_name="item_works", blank=False, null=False, on_delete=models.CASCADE)

    summary = models.CharField(max_length=255, blank=False, null=False)

    content = MarkdownField(
        blank=False,
        null=False,
        help_text="Markdown is supported.",
        rendered_field="content_rendered",
        validator=VALIDATOR_CLASSY,
    )
    content_rendered = RenderedMarkdownField()

    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Work done on {self.created_at}"

    class Meta(object):
        ordering = ("created_at",)  # latest last
        verbose_name = "Work log"
        verbose_name_plural = "Work logs"


class ItemRelated(models.Model):
    item = models.ForeignKey(Item, related_name="related_items", blank=False, null=False, on_delete=models.CASCADE)
    related = models.ForeignKey(
        Item, verbose_name="item", blank=False, null=False, on_delete=models.CASCADE, related_name="related_items_item"
    )

    def __str__(self):
        return self.related.__str__()


class ItemLinks(models.Model):
    item = models.ForeignKey(Item, related_name="item_links", blank=False, null=False, on_delete=models.CASCADE)
    url = models.URLField(blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.url


class ItemPicture(models.Model):
    item = models.ForeignKey(Item, related_name="item_pictures", blank=False, null=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.FileField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file", processors=[ResizeToFit(50, 50, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_small = ImageSpecField(
        source="file", processors=[ResizeToFit(200, 150, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_medium = ImageSpecField(
        source="file", processors=[ResizeToFit(400, 400, upscale=False)], format="JPEG", options={"quality": 80}
    )

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    def __str__(self):
        return self.description or "No description"


class ItemFile(models.Model):
    item = models.ForeignKey(Item, related_name="item_files", blank=False, null=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="pictures/", validators=[validate_other], blank=False, null=False)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        return self.description or "No description"
