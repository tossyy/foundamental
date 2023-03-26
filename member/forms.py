from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CounselorCreationForm(UserCreationForm):
    age = forms.IntegerField(label='年齢')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'password1', 'password2']


class EntrepreneurCreationForm(UserCreationForm):
    companyName = forms.CharField(label='会社名',
                                  max_length=255,
                                  required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'companyName', 'password1', 'password2']


class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser


class CounselorAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = CustomUserChangeForm
    add_form = CounselorCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
