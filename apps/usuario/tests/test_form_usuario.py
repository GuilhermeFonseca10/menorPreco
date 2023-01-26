from django.test import TestCase
from usuario.forms import Usuario

class TestUsuarioForm(TestCase):
    
    def test_form_valid(self):
        form_data = {'field1': 'value1', 'field2': 'value2'}
        form = Usuario(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_form_invalid(self):
        form_data = {'field1': '', 'field2': 'value2'}
        form = Usuario(data=form_data)
        self.assertFalse(form.is_valid())





