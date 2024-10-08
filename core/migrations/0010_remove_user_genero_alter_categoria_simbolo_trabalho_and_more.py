# Generated by Django 5.0.6 on 2024-08-13 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_user_categoria_user_genero"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="genero",
        ),
        migrations.AlterField(
            model_name="categoria",
            name="simbolo",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="Trabalho",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data", models.DateField()),
                ("prazo", models.DateField()),
                ("DataTermino", models.DateField()),
                ("preco", models.DecimalField(decimal_places=1, max_digits=3)),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usuarios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Genero",
        ),
    ]
