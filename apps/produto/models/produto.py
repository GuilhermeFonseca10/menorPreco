from django.db import models
from django.urls import reverse


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
    supermercados = models.ForeignKey(
        "supermercado.Supermercado",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    @property
    def get_absolute_url(self):
        return reverse("produto_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("produto_delete", args=[str(self.id)])
