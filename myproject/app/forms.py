from django import forms
from .models import Driver, Booking

from django import forms
from .models import Driver, Booking


class DriverForm(forms.ModelForm):
    CITY_CHOICES = [
        ('تهران', 'تهران'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),
        ('مشهد', 'مشهد'),
    ]

    city = forms.ChoiceField(choices=CITY_CHOICES, label="شهر")
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="تاریخ"
    )

    class Meta:
        model = Driver
        fields = ['username', 'image', 'city', 'date', 'phone', 'name', 'vehicle_model', 'vehicle_type']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'phone', 'start_location', 'destination', 'travel_date']
