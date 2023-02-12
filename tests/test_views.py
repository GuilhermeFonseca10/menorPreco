from django.urls import reverse_lazy

# from tests.factories import UserFactory
from tests.test_base import MenorPrecoBase


class BaseViewsTest(MenorPrecoBase):
    # def test_model_user(self):
    #     user = UserFactory()
    #     pass

    def test_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("home"), follow=True)
        assert response.status_code == 200

    def test_dashboard_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("dashboard"), follow=True)
        assert response.status_code == 200

        # ------------------ TESTANDO APP SUPERMERCADO VIEWS -----------------

    def test_supermercado_create_view_return_status_code_200_ok(self):
        response = self.client.post(
            reverse_lazy("supermercado_create"), follow=True
        )
        assert response.status_code == 200

    def test_supermercado_list_view_return_status_code_200_ok(self):
        response = self.client.get(
            reverse_lazy("supermercado_list"), follow=True
        )
        assert response.status_code == 200

    # ------------------ TESTANDO APP USUARIO VIEWS ----------------------

    def test_register_view_return_status_code_200_ok(self):
        response = self.client.post(
            reverse_lazy("usuario:register"), follow=True
        )
        assert response.status_code == 200

    def test_usuario_list_view_returns_200_status(self):
        response = self.client.get(
            reverse_lazy("usuario:usuario_list"), follow=True
        )
        assert response.status_code == 200

    def test_get_queryset(self):
        response = self.client.get(reverse_lazy("usuario:usuario_list"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url, follow=True)

    def test_get_queryset_supermercado(self):
        url = reverse_lazy("supermercado_detail", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    # def test_supermercado_detail_view(self):
    #     response = self.client.get(
    #         reverse_lazy("supermercado_detail", kwargs={"id": id})
    #     )
    #     assert response.status_code == 200
