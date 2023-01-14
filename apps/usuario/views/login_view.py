from django.views.generic.base import TemplateView

class LoginView(TemplateView):

    template_name = "usuario/login.html"