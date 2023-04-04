from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class CounselorCreationForm(UserCreationForm):
    age = forms.IntegerField(label='年齢')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'password1', 'password2', ]


class EntrepreneurCreationForm(UserCreationForm):
    companyName = forms.CharField(label='会社名',
                                  max_length=255,
                                  required=True)

    counselor = forms.ChoiceField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'companyName', 'counselor', 'password1', 'password2', ]

    def __init__(self, counselors=None, *args, **kwargs):
        self.base_fields["counselor"].choices = counselors
        super().__init__(*args, **kwargs)


class AdminCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', ]
