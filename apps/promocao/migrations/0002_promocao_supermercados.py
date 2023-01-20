# Generated by Django 4.1.5 on 2023-01-20 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("supermercado", "0002_alter_supermercado_options"),
        ("promocao", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocao",
            name="supermercados",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="supermercado.supermercado",
            ),
        ),
    ]