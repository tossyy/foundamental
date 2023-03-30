from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .forms import *


class OnlyAdminMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.request.user.userType == 'AD'


class RegisterView(LoginRequiredMixin, OnlyAdminMixin, generic.TemplateView):
    template_name = 'register.html'


class CustomLoginView(LoginView):
    template_name = 'account/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'


class CounselorCreateView(LoginRequiredMixin, OnlyAdminMixin, generic.CreateView):
    template_name = 'account/counselor_signup.html'
    form_class = CounselorCreationForm
    success_url = reverse_lazy('member:register')

    def form_valid(self, form):
        # カスタムユーザー
        user = form.save(commit=False)
        user.userType = 'CO'
        user.save()

        # カウンセラーディテール
        counselor = UserDetailCounselor()
        counselor.user_id = user.id
        counselor.age = form.cleaned_data['age']
        counselor.save()

        return super().form_valid(form)


class EntrepreneurCreateView(LoginRequiredMixin, OnlyAdminMixin, generic.CreateView):
    template_name = 'account/entrepreneur_signup.html'
    form_class = EntrepreneurCreationForm
    success_url = reverse_lazy('member:register')

    def form_valid(self, form):
        # カスタムユーザー
        user = form.save(commit=False)
        user.userType = 'EN'
        user.save()

        # 起業家ディテール
        entrepreneur = UserDetailEntrepreneur()
        entrepreneur.user_id = user.id
        entrepreneur.companyName = form.cleaned_data['companyName']
        entrepreneur.save()

        return super().form_valid(form)


class AdminCreateView(LoginRequiredMixin, OnlyAdminMixin, generic.CreateView):
    template_name = 'account/admin_signup.html'
    form_class = AdminCreationForm
    success_url = reverse_lazy('member:register')

    def form_valid(self, form):
        # カスタムユーザー
        user = form.save(commit=False)
        user.userType = 'AD'
        user.save()

        # 起業家ディテール
        admin = UserDetailAdmin()
        admin.user_id = user.id
        admin.save()

        return super().form_valid(form)
