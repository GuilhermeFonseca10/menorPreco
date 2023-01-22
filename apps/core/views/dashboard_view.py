from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin


class DashboardView(TemplateView):

    template_name = "core/dashboard.html"
