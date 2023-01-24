from django.urls import reverse
from django.test import TestCase 

class TestUsuarioUrls(TestCase):

    def test_usuario_urls(self):
        response_200 = reverse('usuario:register')
        self.assertEqual(response_200, "/usuario/register/")
    
    # def test_view_login(self):
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "usuario/login.html")