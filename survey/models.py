from django.db import models

from accounts.models import CustomUser


class Survey(models.Model):
    """サーベイ"""
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='回答日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Survey'

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'


class Question(models.Model):
    """質問"""
    title = models.CharField(verbose_name='タイトル', max_length=255)

    def __str__(self):
        return self.title


class Answer(models.Model):
    """回答"""
    survey = models.ForeignKey(Survey, verbose_name='調査', on_delete=models.PROTECT)
    question = models.ForeignKey(Question, verbose_name='質問', on_delete=models.PROTECT)
    data = models.IntegerField(verbose_name='回答')

    def __str__(self):
        return f'{self.survey.id} - {self.question.id}'
