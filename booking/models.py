import time

from django.db import models

from accounts.models import CustomUser


class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', related_name='available_schedules', null=False, blank=False, on_delete=models.PROTECT)
    entrepreneur = models.ForeignKey(CustomUser, verbose_name='予約者', related_name='booked_schedules', null=True, blank=False, on_delete=models.PROTECT, default=None)
    startTime = models.DateTimeField(verbose_name='開始時間', null=False, blank=False)
    endTime = models.DateTimeField(verbose_name='終了時間', null=False, blank=False)

    def __str__(self):
        return f'{self.startTime} - {self.user}'

    @property
    def get_timerange(self):
        return self.startTime.strftime('%Y/%m/%d %H:%M') + '~' + self.endTime.strftime('%H:%M')
