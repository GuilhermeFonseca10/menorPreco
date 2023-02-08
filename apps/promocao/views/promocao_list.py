from django.views.generic import ListView
from promocao.models.promocao import Promocao


class PromocaoListView(ListView):
    model = Promocao
    template_name = "promocao/promocao_list.html"

    def promocao(self):

        promocao = Promocao.objects.all()

        return promocao
