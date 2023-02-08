from django.urls import reverse
from tests.test_base import MenorPrecoBase


class BaseUrlsTest(MenorPrecoBase):
    def test_home_urls(self):
        url = reverse("home")
        self.assertEqual(url, "/")

    def test_dashboard_urls(self):
        url = reverse("dashboard")
        self.assertEqual(url, "/dashboard/")

    def test_login_urls(self):
        url = reverse("login")
        self.assertEqual(url, "/login/")

    def test_register_urls(self):
        url = reverse("usuario:register")
        self.assertEqual(url, "/usuario/register/")

    def test_usuario_list_urls(self):
        url = reverse("usuario:usuario_list")
        self.assertEqual(url, "/usuario/list/")

    def test_supermercado_list_urls(self):
        url = reverse("supermercado_list")
        self.assertEqual(url, "/supermercado/list")

    def test_supermercado_urls(self):
        url = reverse("supermercado_create")
        self.assertEqual(url, "/supermercado/cad")

    # def test_produto_urls(self):
    #    url = reverse('produto_list')
    #    self.assertEqual(url, '/produto/list')
