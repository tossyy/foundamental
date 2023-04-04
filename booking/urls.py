from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('schedule-list/', views.ScheduleListView.as_view(), name='schedule-list'),
    path('schedule-create/', views.ScheduleCreateView.as_view(), name='schedule-create'),
    path('schedule-delete/<int:pk>', views.ScheduleDeleteView.as_view(), name='schedule-delete'),
    path('schedule-booking/<int:pk>', views.ScheduleBookingView.as_view(), name='schedule-booking'),
    path('make-booking/', views.make_booking, name="make-booking"),
]
