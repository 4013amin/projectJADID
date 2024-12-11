from django import forms
from .models import Driver, Booking


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['username', 'phone', 'name' , 'vehicle_model' , 'vehicle_type']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'phone', 'start_location', 'destination', 'travel_date']
