from django import forms

from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter

from .models import CustomUser, UserType


class CounselorSignUpForm(SignupForm):
    userType = forms.ChoiceField(label='ユーザータイプ',
                                 choices=UserType.choices,
                                 required=True)
    age = forms.IntegerField(label='年齢')

    class Meta:
        model = CustomUser


class EntrepreneurSignUpForm(SignupForm):
    userType = forms.ChoiceField(label='ユーザータイプ',
                                 choices=UserType.choices,
                                 required=True)
    companyName = forms.CharField(label='会社名',
                                  max_length=255,
                                  required=True)

    class Meta:
        model = CustomUser
