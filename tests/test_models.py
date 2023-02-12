from apps.usuario.models import Usuario
from tests.test_base import MenorPrecoBase


class BaseModelsTest(MenorPrecoBase):
    def test_model_user(self):
        user = self.test_create_user()
        self.assertEqual(user.username, str(user))

    def test_get_full_name(self):
        self.user = Usuario.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.user.save()
        self.user = Usuario.objects.get(id=self.user.id)
        return self.user
