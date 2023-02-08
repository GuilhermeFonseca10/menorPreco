from django.views.generic import CreateView
from promocao.forms.promocao_create_form import PromocaoForm
from promocao.models.promocao import Promocao
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class PromocaoCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    model = Promocao
    allowed_roles = "administrador"
    template_name = "promocao/promocao_form.html"

    form_class = PromocaoForm

    success_url = "/dashboard"
