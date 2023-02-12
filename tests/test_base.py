# from django.contrib.auth.models import User
# from apps.usuario.models.usuario import Usuario
from apps.usuario.models import Usuario
from django.test import TestCase


class MenorPrecoBase(TestCase):
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()

    def test_create_user(self):
        user = Usuario.objects.create(
            username="testuser", email="testuser@example.com"
        )
        user.save()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        return user

    def test_caracter_full(self):
        user = Usuario.objects.create(
            username="testuser", email="testuser@example.com"
        )
        user.save()
        return user

    def test_create_string(self):
        self.user = Usuario.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.user.save()
        self.user = Usuario.objects.get(id=self.user.id)
        return self.user
