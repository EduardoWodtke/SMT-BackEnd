# Generated by Django 5.0.6 on 2024-07-30 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_user_cpf_user_descricao_user_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="categoria",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, related_name="autores", to="core.categoria"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="genero",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.PROTECT, related_name="generos", to="core.genero"
            ),
            preserve_default=False,
        ),
    ]
