# Generated by Django 3.1.4 on 2020-12-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Manufacturer name'),
        ),
    ]
