from django.urls import path

from . import views

app_name = 'member'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('counselor_signup/', views.CounselorCreateView.as_view(), name='counselor_signup'),
    path('entrepreneur_signup/', views.EntrepreneurCreateView.as_view(), name='entrepreneur_signup'),
    path('admin_signup/', views.AdminCreateView.as_view(), name='admin_signup'),
]
