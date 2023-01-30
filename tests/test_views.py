from django.urls import reverse_lazy
from test_base import MenorPrecoBase

 #  ---------------------------- TESTANDO VIEWS --------------------------------------   
   
class BaseViewsTest(MenorPrecoBase):


    def test_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("home"),follow=True)
        assert response.status_code == 200
        
    def test_dashboard_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("dashboard"),follow=True)
        assert response.status_code == 200
        
    def test_produto_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("produto_list"),follow=True)
        assert response.status_code == 200
        

    def test_supermercado_create_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("supermercado_create"),follow=True)
        assert response.status_code == 200
        
    def test_supermercado_list_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("supermercado_list"),follow=True)
        assert response.status_code == 200
        

    def test_register_view_return_status_code_200_ok(self):
        response = self.client.post(reverse_lazy("usuario:register"),follow=True)
        assert response.status_code == 200
        

    def test_usuario_list_view_return_status_code_200_ok(self):
        response = self.client.get(reverse_lazy("usuario:usuario_list"),follow=True)
        assert response.status_code == 200
        