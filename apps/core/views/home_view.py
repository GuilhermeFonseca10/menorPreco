from django.views.generic import ListView
from produto.models.produto import Produto


class HomeView(ListView):

    model = Produto

    def produto(self):

        produto = Produto.objects.all()

        return produto

    template_name = "core/home.html"
