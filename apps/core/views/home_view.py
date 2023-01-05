from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin


class HomeView(TemplateView):

    template_name = "core/home.html"
