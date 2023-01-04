from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# User = get_user_model()


class CustomUser(AbstractUser):

    def __str__(self):
        return self.get_full_name()

