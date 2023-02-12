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

    # ------------------ TESTANDO APP USUARIO URLS ----------------------

    def test_register_urls(self):
        url = reverse("usuario:register")
        self.assertEqual(url, "/usuario/register/")

    def test_usuario_list_urls(self):
        url = reverse("usuario:usuario_list")
        self.assertEqual(url, "/usuario/list/")

        # ------------------ TESTANDO APP SUPERMERCADO URLS -----------------

    def test_supermercado_list_urls(self):
        url = reverse("supermercado_list")
        self.assertEqual(url, "/supermercado/list")

    def test_supermercado_urls(self):
        url = reverse("supermercado_create")
        self.assertEqual(url, "/supermercado/cad")

    def test_supermercado_detail_url(self):
        url = reverse("supermercado_detail", args=[1])
        self.assertEqual(url, "/supermercado/detail/1/")

    def test_supermercado_update_url(self):
        url = reverse("supermercado_update", args=[1])
        self.assertEqual(url, "/supermercado/update/1/")
