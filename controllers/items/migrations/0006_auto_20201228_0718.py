# Generated by Django 3.1.4 on 2020-12-28 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0005_itemweight_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(blank=True, help_text="Markdown is supported."),
        ),
        migrations.AlterField(
            model_name="item",
            name="plate_infos",
            field=models.TextField(blank=True, help_text="Markdown is supported.", null=True),
        ),
        migrations.CreateModel(
            name="ItemPower",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("mode", models.CharField(max_length=255)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="item_modes", to="items.item"
                    ),
                ),
            ],
            options={
                "ordering": ("mode",),
            },
        ),
    ]