from django.contrib.auth.models import AbstractUser


class Counselor(AbstractUser):

    class Meta:
        verbose_name_plural = 'Counselor'
        