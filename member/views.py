from django.views import generic
from django.urls import reverse_lazy

from .forms import *


class RegisterView(generic.TemplateView):
    template_name = 'register.html'


class CounselorCreateView(generic.CreateView):
    template_name = 'account/counselor_signup.html'
    form_class = CounselorCreationForm
    success_url = reverse_lazy('member:register')

    def form_valid(self, form):
        user = form.save()



class EntrepreneurCreateView(generic.CreateView):
    template_name = 'account/entrepreneur_signup.html'
    form_class = EntrepreneurCreationForm
    success_url = reverse_lazy('member:register')


class AdminCreateView(generic.FormView):
    template_name = 'account/admin_signup.html'
    form_class = AdminSignUpForm
    success_url = reverse_lazy('member:register')

