from django.db import models

from accounts.models import CustomUser


class Survey(models.Model):
    """サーベイ"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', blank=False, null=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='回答日時', auto_now_add=True)

    answer1 = models.IntegerField(verbose_name='最近調子はどうですか', blank=False, null=False)
    answer2 = models.IntegerField(verbose_name='幸せですか', blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Survey'

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
