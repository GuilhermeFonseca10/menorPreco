from produto.models.produto import Produto
from rest_framework.serializers import ModelSerializer


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            "id",
            "nome",
            "valor",
            "estoque",
            "imagem",
            "descricao",
            "supermercados",
        ]
