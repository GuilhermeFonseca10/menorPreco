from produto.models.produto import Produto
from produto.serializers.produto_serializer import ProdutoSerializer
from rest_framework.viewsets import ModelViewSet


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def create(self, request, *args, **kwargs):
        return super(ProdutoViewSet, self).create(request, *args, **kwargs)
