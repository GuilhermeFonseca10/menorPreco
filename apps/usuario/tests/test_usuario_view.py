from django.test import TestCase, Client
from django.urls import reverse


class TestUsuarioView(TestCase):
    
    def test_usuario_view(self):
        client = Client()
        response = client.get(reverse('usuario_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response)



