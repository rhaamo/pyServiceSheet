# Generated by Django 3.1.4 on 2020-12-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0020_auto_20201228_1055"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="short_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]