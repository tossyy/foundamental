from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    userType = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f'{self.username} - {self.userType}'


class UserType(models.TextChoices):
    COUNSELOR = 'CO', 'counselor'
    ENTREPRENEUR = 'EN', 'entrepreneur'
    ADMIN = 'AD', 'admin'


class UserDetailCounselor(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_counselor',
                                on_delete=models.CASCADE)

    age = models.IntegerField(verbose_name='年齢', null=False, blank=False)


class UserDetailEntrepreneur(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_entrepreneur',
                                on_delete=models.CASCADE)

    companyName = models.CharField(verbose_name='会社名', max_length=255, null=False, blank=False)


class UserDetailAdmin(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_admin',
                                on_delete=models.CASCADE)
