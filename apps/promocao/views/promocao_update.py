from django.urls import reverse_lazy
from django.views.generic import UpdateView
from promocao.models.promocao import Promocao
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class PromocaoUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    model = Promocao
    allowed_roles = "administrador"
    template_name = "promocao/promocao_form.html"
    fields = [
        "nome",
        "supermercados",
    ]
    success_url = reverse_lazy("promocao_detail_admin")

    def get_success_url(self):
        return reverse_lazy("promocao_detail_admin", args=(self.object.pk,))
