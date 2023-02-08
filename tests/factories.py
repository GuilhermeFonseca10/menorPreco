import factory
from faker import Faker
from usuario.models.usuario import Usuario


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    username = factory.Faker("nome")
    email = factory.Faker("email")
    cpf = factory.Faker("cpf")
    password = factory.Faker("password")
