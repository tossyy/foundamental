from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('counselor_signup/', views.CounselorSignUpView.as_view(), name='counselor_signup'),
    path('entrepreneur_signup/', views.EntrepreneurSignUpView.as_view(), name='entrepreneur_signup'),
    path('admin_signup/', views.AdminSignUpView.as_view(), name='admin_signup'),
]
