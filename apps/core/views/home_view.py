from core.filters import FilterBook
from django.views.generic import ListView
from produto.models.produto import Produto
from rolepermissions.mixins import HasRoleMixin

from utils.decorators import LoginRequiredMixin


class HomeView(HasRoleMixin, LoginRequiredMixin, ListView):

    model = Produto
    template_name = "core/home.html"
    filterset = FilterBook
    paginate_by = 3
    allowed_roles = ["usuario_comum", "administrador"]

    def get_queryset(self):
        queryset = super().get_queryset().all()
        self.filterset = self.filterset(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context


# def produto(self):

# return Produto.objects.all()

# def get_context_data(self, **kwargs):
# context = super().get_context_data(**kwargs)
# produtos = self.produto()
# paginator = Paginator(produtos, self.paginate_by)
# page = self.request.GET.get("page")
# context["produto_list"] = paginator.get_page(page)
# return context
