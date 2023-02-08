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
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")


# from django.contrib.auth.models import User
# from django.test import TestCase


# class MenorPrecoBase(TestCase):
#     def setUp(self) -> None:
#         return super().setUp

#     def tearDown(self) -> None:
#         return super().tearDown()

#     def create_user(self):
#         user = User.objects.create(
#             username="teste",
#             email="teste@example.com",
#             cpf="123.456.789-00",
#             password="t1234567.",
#         )
#         user.save()
#         return user

#     def login(self):
#         user_logged = self.cliente.login(
#             email="test@hotmail.com", password="t1234567."
#         )
#         return user_logged
