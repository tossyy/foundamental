from django.urls import path

from . import views

app_name = 'survey'
urlpatterns = [
    path('answer/', views.AnswerView.as_view(), name='answer'),
]
