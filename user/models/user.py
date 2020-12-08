from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

def Kylie():
    return User.objects.filter(email="kylie.a@protonmail.com").first()
