from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Categoria")

    supermercados = models.ForeignKey(
        "supermercado.Supermercado",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    @property
    def get_absolute_url(self):
        return reverse("categoria_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("categoria_delete", args=[str(self.id)])
