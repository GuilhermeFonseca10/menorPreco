# Generated by Django 4.1.5 on 2023-01-20 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("supermercado", "0002_alter_supermercado_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="supermercado",
            name="usuario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
