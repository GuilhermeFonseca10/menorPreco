import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")


# from apps.usuario.models.usuario import Usuario
# from factory.django import DjangoModelFactory
# from faker import Faker


# class UserFactory(DjangoModelFactory):
#     username = Faker("nome")
#     email = Faker("email")

#     class Meta:
#         model = Usuario
