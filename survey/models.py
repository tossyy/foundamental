from django.db import models

from member.models import CustomUser


class Answer(models.Model):
    """回答モデル"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

