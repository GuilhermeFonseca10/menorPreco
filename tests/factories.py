from factory.django import DjangoModelFactory
from faker import Faker
from apps.usuario.models import Usuario

class UserFactory(DjangoModelFactory):
    username = Faker("user_name") 
    email = Faker("email")
    cpf = Faker("cpf")
    password = Faker("password")
    
    class Meta:
        model = Usuario