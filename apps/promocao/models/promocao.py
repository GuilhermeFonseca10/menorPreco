from django.db import models


class Promocao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Promoção")
    produtos = models.ManyToManyField(
        "produto.Produto", verbose_name="Produto", blank=True
    )

    class Meta:
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
