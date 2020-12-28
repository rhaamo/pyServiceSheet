# Generated by Django 3.1.4 on 2020-12-28 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0015_auto_20201228_0807"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="itemfile",
            options={"ordering": ("id",), "verbose_name": "File", "verbose_name_plural": "Files"},
        ),
        migrations.AlterModelOptions(
            name="itempicture",
            options={"ordering": ("id",), "verbose_name": "Picture", "verbose_name_plural": "Pictures"},
        ),
        migrations.AlterModelOptions(
            name="itemwork",
            options={"ordering": ("created_at",), "verbose_name": "Work log", "verbose_name_plural": "Work logs"},
        ),
    ]