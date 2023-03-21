from django.views import generic


class CounselorSignUpView(generic.TemplateView):
    template_name = 'account/counselor_signup.html'


class EntrepreneurSignUpView(generic.TemplateView):
    template_name = 'account/entrepreneur_signup.html'
