from django import forms

from .models import *


class SurveyCreateForm(forms.ModelForm):

    class Meta:
        model = Survey
        exclude = ('user', 'created_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
