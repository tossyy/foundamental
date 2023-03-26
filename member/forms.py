from django import forms

from allauth.account.forms import SignupForm

from .models import CustomUser


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
