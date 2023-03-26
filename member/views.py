from django.views import generic

from .forms import *


class RegisterView(generic.TemplateView):
    template_name = 'register.html'


class CounselorSignUpView(generic.FormView):
    template_name = 'account/counselor_signup.html'
    form_class = CounselorSignUpForm


class EntrepreneurSignUpView(generic.FormView):
    template_name = 'account/entrepreneur_signup.html'
    form_class = EntrepreneurSignUpForm


class AdminSignUpView(generic.FormView):
    template_name = 'account/admin_signup.html'
    form_class = AdminSignUpForm

