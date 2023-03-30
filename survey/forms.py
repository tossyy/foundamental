from django import forms

from .models import *


class SurveyCreateForm(forms.ModelForm):

    answer1 = forms.IntegerField(label='質問１')
    answer2 = forms.IntegerField(label='質問２')

    class Meta:
        model = Survey
        fields = ['answer1', 'answer2']
