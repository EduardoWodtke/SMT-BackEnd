# Generated by Django 5.0.6 on 2024-08-16 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_rename_datainicio_trabalho_datainicio_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
