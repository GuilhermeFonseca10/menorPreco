from django.db import models


class Supermercado(models.Model):
    """
    A classe Supermercado serve para armazernar os(as) supermercados do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Supermercado.
    """

    nome = models.CharField(verbose_name="Nome", max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "supermercado"
        verbose_name = "Supercado"
        verbose_name_plural = "Supermercado"
