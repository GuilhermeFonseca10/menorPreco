from django.db import models
from django.urls import reverse


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

    @property
    def get_absolute_url(self):
        return reverse("promocao_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("promocao_delete", args=[str(self.id)])
