# Generated by Django 3.1.4 on 2020-12-30 09:21

import controllers.items.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0021_item_short_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itempicture",
            name="file",
            field=models.ImageField(upload_to="pictures/", validators=[controllers.items.validators.validate_picture]),
        ),
    ]