from django.urls import reverse_lazy
from .factories import UserFactory
from tests.test_base import MenorPrecoBase

 #  ---------------------------- TESTANDO VIEWS --------------------------------------   
   
class BaseModelsTest(MenorPrecoBase):
    def setUp(self) -> None:
        return super().setUp()

    def test_user_creation(self):
        user = UserFactory()
        self.assertIsNotNone(user.pk)
        self.assertTrue(user.check_password('password'))