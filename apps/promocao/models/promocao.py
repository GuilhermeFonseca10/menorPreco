from django.db import models


class Promocao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Promoção")

    supermercados = models.ForeignKey(
        "supermercado.Supermercado",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
