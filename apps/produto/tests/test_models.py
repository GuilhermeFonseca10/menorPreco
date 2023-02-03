from django.test import TestCase
from produto.models.categoria import Categoria

class TestModelsProduto(TestCase):
    def test_create_produto(self):
        categoria = Categoria.objects.create(
            nome= "TesteCategoria"
        )
        self.assertEqual(categoria.nome, "TesteCategoria")
