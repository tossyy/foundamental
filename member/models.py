from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """カスタムユーザーモデル"""

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    userType = models.CharField(max_length=10, null=False, blank=False)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('custom user')
        verbose_name_plural = _('custom user')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        """username属性のゲッター

        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email

    def __str__(self):
        return f'{self.email} - {self.userType}'


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
