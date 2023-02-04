from django.db import models


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
