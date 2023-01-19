
import datetime
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestViews(TestCase): 

    def test_views_status(self):
        response = self.client.get(reverse("usuario/register.html"))
        self.assertEqual(response.status_code, 200)