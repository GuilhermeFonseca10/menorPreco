from django.views.generic import CreateView

from apps.supermercado.forms.supermercado_create_form import SupermercadoForm
from utils.decorators import LoginRequiredMixin

from ..models.supermercado import Supermercado


class SupermercadoCreateView(LoginRequiredMixin, CreateView):
    model = Supermercado

    def get_queryset(self):
        usuario = self.request.user.id

        return Supermercado.objects.filter(usuario=usuario)

    form_class = SupermercadoForm

    success_url = "list"
