# Generated by Django 5.0.6 on 2024-07-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_categoria_simbolo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="simbolo",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
