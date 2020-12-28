from django.db import models
import uuid


class Manufacturer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    name = models.CharField(verbose_name="Manufacturer name", max_length=255)
    notes = models.TextField(unique=False, blank=True)

    def __str__(self):
        return self.name
