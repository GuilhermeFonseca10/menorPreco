# Generated by Django 4.1.4 on 2023-01-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, verbose_name="Categoria")),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "ordering": ["nome"],
            },
        ),
    ]
