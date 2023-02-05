from django.views.generic import CreateView
from produto.forms.categora_create_form import CategoriaForm

from utils.decorators import LoginRequiredMixin

from ..models.categoria import Categoria


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"

    form_class = CategoriaForm

    success_url = "/dashboard"
