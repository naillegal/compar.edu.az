from django.forms import ModelForm
from promotion.models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'contact', 'subject', 'message')