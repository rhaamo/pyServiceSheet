# Generated by Django 3.1.4 on 2020-12-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0012_auto_20201228_0757"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemlinks",
            name="notes",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]