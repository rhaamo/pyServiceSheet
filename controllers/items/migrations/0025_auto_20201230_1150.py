# Generated by Django 3.1.4 on 2020-12-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0024_auto_20201230_1035"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemweight",
            name="notes",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
