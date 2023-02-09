from django.views.generic import ListView
from promocao.models.promocao import Promocao

from utils.decorators import LoginRequiredMixin


class PromocaoListView(LoginRequiredMixin, ListView):
    model = Promocao

    template_name = "promocao/promocao_list.html"

    def promocao(self):

        promocao = Promocao.objects.all()

        return promocao
