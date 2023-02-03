from django.contrib.auth.models import User
from django.test import TestCase


class  MenorPrecoBase(TestCase):
    
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()
    
    
    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        cpf = '123.456.789-00',
        password='t1234567.',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'test@hotmail.com', password = 't1234567.')
        return user_logged
    
    