from django import forms
from django.utils import timezone

from .models import Schedule


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('startTime', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['startTime'].input_formats = ['%Y/%m/%d %H:%M']

        self.fields['startTime'].widget.attrs = {
            'class': 'form-control',
        }


class MakeBookingForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('entrepreneur', )