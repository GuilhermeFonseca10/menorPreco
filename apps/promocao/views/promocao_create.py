from django.views.generic import CreateView
from promocao.forms.promocao_create_form import PromocaoForm
from promocao.models.promocao import Promocao

from utils.decorators import LoginRequiredMixin


class PromocaoCreateView(LoginRequiredMixin, CreateView):
    model = Promocao
    template_name = "promocao/promocao_form.html"

    form_class = PromocaoForm

    success_url = "/dashboard"
