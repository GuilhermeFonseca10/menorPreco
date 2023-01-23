from django.views.generic import ListView
from usuario.models.usuario import Usuario

from utils.decorators import LoginRequiredMixin


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario

    def get_queryset(self):
        usuario_id = self.request.user.id

        return Usuario.objects.filter(id=usuario_id)

    # template_name = "usuario/usuario_list.html"
