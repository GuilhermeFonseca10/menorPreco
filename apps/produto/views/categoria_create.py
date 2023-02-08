from django.views.generic import CreateView
from produto.forms.categora_create_form import CategoriaForm
from rolepermissions.mixins import HasRoleMixin
from utils.decorators import LoginRequiredMixin

from ..models.categoria import Categoria


class CategoriaCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    model = Categoria
    allowed_roles = "administrador"
    template_name = "categoria/categoria_form.html"

    form_class = CategoriaForm

    success_url = "/dashboard"
