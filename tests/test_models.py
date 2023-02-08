from tests.factories import UserFactory
from tests.test_base import MenorPrecoBase


class BaseModelsTest(MenorPrecoBase):
    def setUp(self) -> None:
        return super().setUp()

    def test_user_creation(self):
        user = UserFactory()
        self.assertIsNotNone(user.pk)

        self.assertTrue(user.check_name("name"))
        self.assertTrue(user.check_email("email"))
