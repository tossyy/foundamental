from django.views import generic

from .forms import *


class CounselorSignUpView(generic.FormView):
    template_name = 'account/counselor_signup.html'
    form_class = CounselorSignUpForm


class EntrepreneurSignUpView(generic.FormView):
    template_name = 'account/entrepreneur_signup.html'
    form_class = EntrepreneurSignUpForm
