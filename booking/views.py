from django.views import generic


class BookingView(generic.TemplateView):
    template_name = 'booking.html'