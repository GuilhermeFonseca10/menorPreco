from django.core.paginator import Paginator
from django.views.generic import ListView
from produto.models.produto import Produto


class HomeView(ListView):

    model = Produto
    template_name = "core/home.html"

    paginate_by = 1

    def produto(self):

        return Produto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = self.produto()
        paginator = Paginator(produtos, self.paginate_by)
        page = self.request.GET.get("page")
        context["produto_list"] = paginator.get_page(page)
        return context
