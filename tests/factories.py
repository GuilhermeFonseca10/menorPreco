import factory

from apps.usuario.models.usuario import Usuario


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario
        app_label = "usuario"

    username = factory.Faker("username")
    email = factory.Faker("email")
    password = factory.Faker("password")
