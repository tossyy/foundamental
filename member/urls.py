from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('counselor_signup/', views.CounselorSignUpView.as_view(), name='counselor_signup'),
    path('entrepreneur_signup/', views.EntrepreneurSignUpView.as_view(), name='entrepreneur_signup')
]
