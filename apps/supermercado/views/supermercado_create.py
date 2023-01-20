from django.views.generic import CreateView
from supermercado.forms.supermercado_create_form import SupermercadoForm
from supermercado.models.supermercado import Supermercado

from utils.decorators import LoginRequiredMixin


class SupermercadoCreateView(LoginRequiredMixin, CreateView):
    model = Supermercado

    form_class = SupermercadoForm

    # fields = ['dispesa', 'valor', 'categorias', 'data', 'conta']

    success_url = "supermercado_list"
