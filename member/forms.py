from django import forms

from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter

from .models import CustomUser, UserType


class CounselorSignUpForm(SignupForm):
    age = forms.IntegerField(label='年齢')

    class Meta:
        model = CustomUser


class EntrepreneurSignUpForm(SignupForm):
    companyName = forms.CharField(label='会社名',
                                  max_length=255,
                                  required=True)

    class Meta:
        model = CustomUser


class AdminSignUpForm(SignupForm):
    class Meta:
        model = CustomUser
