from django.db import models

from .categoria import Categoria


class Produto(models.Model):

    nome = models.CharField(verbose_name="Produto", max_length=100)
    valor = models.DecimalField(
        verbose_name="Valor", max_digits=10, decimal_places=2, default=0
    )
    estoque = models.IntegerField(verbose_name="Estoque")
    imagem = models.ImageField(
        verbose_name="Imagem", upload_to="produto/produtos/"
    )
    descricao = models.TextField(verbose_name="Descrição", blank=True)
    criado = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado em", auto_now=True)

    categorias = models.ManyToManyField(
        "Categoria", verbose_name="Categorias", blank=True
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
