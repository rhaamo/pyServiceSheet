# Generated by Django 3.1.4 on 2020-12-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0007_itemworks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemworks",
            name="content",
            field=models.TextField(help_text="Markdown is supported."),
        ),
    ]
