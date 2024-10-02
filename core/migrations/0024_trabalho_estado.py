# Generated by Django 5.0.6 on 2024-09-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_user_tipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="trabalho",
            name="estado",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Negocio"), (2, "Em andamento"), (3, "Concluido"), (4, "Pago")],
                default=1,
                null=True,
            ),
        ),
    ]