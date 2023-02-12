from django.db import models
from django.urls import reverse


class Supermercado(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)
    imagem = models.ImageField(
        null=True,
        verbose_name="Imagem",
        upload_to="supermercado/supermercados/",
    )
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    cnpj = models.CharField(verbose_name="CNPJ", max_length=14)
    cep = models.CharField(verbose_name="CEP", max_length=11)
    cidade = models.CharField(verbose_name="Cidade", max_length=100)
    bairro = models.CharField(verbose_name="Bairro", max_length=11)
    rua = models.CharField(verbose_name="Rua", max_length=100)
    numero = models.IntegerField(verbose_name="Número")
    date_joined = models.DateTimeField("Data de Entrada", auto_now_add=True)

    usuario = models.ForeignKey(
        "usuario.Usuario", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "supermercado"
        verbose_name = "Supermercado"
        verbose_name_plural = "Supermercados"

    @property
    def get_absolute_url(self):
        return reverse("supermercado_update", args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse("supermercado_delete", args=[str(self.id)])
