from django.urls import path

from . import views

app_name = 'survey'
urlpatterns = [
    path('survey/', views.SurveyCreateView.as_view(), name='survey'),
]
