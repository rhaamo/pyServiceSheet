# Generated by Django 3.1.4 on 2020-12-28 08:05

import controllers.items.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0013_itemlinks_notes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="itemlinks",
            old_name="notes",
            new_name="description",
        ),
        migrations.CreateModel(
            name="ItemPictures",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "file",
                    models.FileField(upload_to="pictures/", validators=[controllers.items.validators.validate_picture]),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="item_pictures", to="items.item"
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="ItemFiles",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "file",
                    models.FileField(upload_to="pictures/", validators=[controllers.items.validators.validate_other]),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="item_files", to="items.item"
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]
