from django.urls import reverse_lazy
from django.views.generic import UpdateView
from produto.models.categoria import Categoria

from utils.decorators import LoginRequiredMixin


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "categoria/categoria_form.html"
    fields = [
        "nome",
        "supermercados",
    ]
    success_url = reverse_lazy("categoria_detail_admin")

    def get_success_url(self):
        return reverse_lazy("categoria_detail_admin", args=(self.object.pk,))
