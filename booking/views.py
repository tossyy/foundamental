import datetime

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Schedule
from .forms import ScheduleCreateForm, MakeBookingForm


class BookingView(LoginRequiredMixin, generic.ListView):
    template_name = 'booking/booking.html'
    model = Schedule

    def get_queryset(self):
        schedules = Schedule.objects.filter(user=self.request.user.detail_entrepreneur.counselor,
                                            startTime__gt=timezone.now()).order_by('startTime')
        return schedules


class ScheduleListView(LoginRequiredMixin, generic.ListView):
    template_name = 'booking/schedule-list.html'
    model = Schedule

    def get_queryset(self):
        schedules = Schedule.objects.filter(user=self.request.user).order_by('startTime')
        return schedules


class ScheduleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Schedule
    template_name = 'booking/schedule-create.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('booking:schedule-list')
    
    def form_valid(self, form):
        schedule = form.save(commit=False)

        schedule.user = self.request.user

        schedule.endTime = schedule.startTime + datetime.timedelta(hours=1)

        schedule.save()

        return super().form_valid(form)


class ScheduleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Schedule
    template_name = 'booking/schedule-delete.html'
    success_url = reverse_lazy('booking:schedule-list')


class ScheduleBookingView(LoginRequiredMixin, generic.DetailView):
    model = Schedule
    template_name = 'booking/schedule-booking.html'


def make_booking(request):
    schedule = Schedule.objects.get(pk=request.POST['pk'])
    schedule.entrepreneur = request.user
    schedule.save()

    return redirect('dashboard:index')
