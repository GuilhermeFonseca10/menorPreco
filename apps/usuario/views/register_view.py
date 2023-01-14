from django.views.generic.base import TemplateView

class RegisterView(TemplateView):

    template_name = "usuario/register.html"