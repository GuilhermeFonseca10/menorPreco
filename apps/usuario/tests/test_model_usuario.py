from django.test import TestCase

from menorPreco.apps.usuario.models.usuario import Usuario


class TestUsuarioModel(TestCase):

    def test_mymodel_fields(self):
        usuario = Usuario.objects.get(field1="value1")
        self.assertEqual(usuario.field1, "value1")
        self.assertEqual(usuario.field2, "value2")
