# Generated by Django 4.1.5 on 2023-02-06 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("promocao", "0003_remove_promocao_produtos"),
        ("produto", "0003_categoria_supermercados"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="promocao",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="promocao.promocao",
            ),
        ),
    ]