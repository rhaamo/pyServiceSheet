# Generated by Django 3.1.4 on 2020-12-28 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("items", "0003_auto_20201228_0653"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemWeight",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("weight", models.FloatField()),
                ("unit", models.CharField(max_length=15)),
                ("notes", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("weight",),
            },
        ),
        migrations.AddField(
            model_name="item",
            name="plate_infos",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="item",
            name="serial_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
                verbose_name="Category",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="country_of_origin",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Country of Origin"),
        ),
    ]
