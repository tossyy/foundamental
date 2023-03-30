from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import *


class OnlyEntrepreneurMixin(UserPassesTestMixin):
    raise_exception = False

    def test_func(self):
        return self.request.user.userType == 'EN'


class AnswerView(LoginRequiredMixin, OnlyEntrepreneurMixin, generic.FormView):
    template_name = 'answer.html'
    success_url = reverse_lazy('dashboard:index')
