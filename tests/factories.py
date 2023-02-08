from factory.django import DjangoModelFactory
from faker import Factory, Faker
from apps.usuario.models import Usuario

class UserFactory(Factory.django.DjangoModelFactory):
    username = Faker("nome") 
    email = Faker("email")
    
    class Meta:
        model = Usuario
        