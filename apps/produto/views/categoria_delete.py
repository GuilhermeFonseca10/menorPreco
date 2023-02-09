from django.views.generic import DeleteView
from produto.models.categoria import Categoria
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class CategoriaDeleteView(HasRoleMixin, LoginRequiredMixin, DeleteView):
    model = Categoria
    allowed_roles = "administrador"
    template_name = "categoria/categoria_confirm_delete.html"
    success_url = "/dashboard"
