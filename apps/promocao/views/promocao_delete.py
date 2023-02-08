from django.views.generic import DeleteView
from promocao.models.promocao import Promocao

from utils.decorators import LoginRequiredMixin


class PromocaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Promocao
    template_name = "promocao/promocao_confirm_delete.html"
    success_url = "/dashboard"
