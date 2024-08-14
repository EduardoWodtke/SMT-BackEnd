# Generated by Django 5.0.6 on 2024-08-14 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_alter_user_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avaliacao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nota", models.DecimalField(decimal_places=1, max_digits=3)),
                ("descricao", models.CharField(max_length=100)),
                (
                    "trabalho",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="trabalhos",
                        to="core.trabalho",
                    ),
                ),
            ],
        ),
    ]
