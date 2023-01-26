from django.urls import reverse
from django.test import TestCase 

class TestUsuarioUrls(TestCase):

    def test_usuario_urls(self):
        response_200 = reverse('usuario:register')
        self.assertEqual(response_200, "/usuario/register/")
    