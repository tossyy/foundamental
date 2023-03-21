from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager


class UserType(models.Model):
    """ ユーザ種別 """
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)

    def __str__(self):
        return f'{self.id} - {self.typename}'


USERTYPE_COUNSELOR = 100
USERTYPE_ENTREPRENEUR = 200
USERTYPE_DEFAULT = USERTYPE_ENTREPRENEUR


class CustomUserManager(UserManager):
    """ 拡張ユーザーモデル向けのマネージャー """

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """ 拡張ユーザーモデル """

    class Meta(object):
        db_table = 'custom_user'

    # 作成したマネージャークラスを使用
    objects = CustomUserManager()

    # モデル内にユーザ種別を持つ
    userType = models.ForeignKey(UserType,
                                 verbose_name='ユーザ種別',
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class UserDetailCounselor(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_counselor',
                                on_delete=models.CASCADE)

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id}'


class UserDetailEntrepreneur(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                db_index=True,
                                related_name='detail_entrepreneur',
                                on_delete=models.CASCADE)

    company_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{user.id} - {user.username} - {user.email} - {self.id}'
