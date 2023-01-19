from django.urls import reverse
from django.test import TestCase 

class TestUsuarioViews(TestCase):

    def test_login(self):
        response_200 = self.client.get(reverse('login'))
        self.assertEqual(response_200.status_code, 200)
        self.assertTemplateUsed(response_200, "usuario/login.html")
    
    # def test_view_login(self):
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "usuario/login.html")