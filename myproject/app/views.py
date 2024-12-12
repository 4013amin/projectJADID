from .models import Driver
from django.shortcuts import render
from .forms import DriverForm
from datetime import date, timedelta


def index(request):
    drivers = Driver.objects.filter(approved=True)
    return render(request, 'home.html', {'drivers': drivers})


def formRegister(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': form, 'success': True})
        else:
            return render(request, 'FormDriver.html', {'form': form, 'errors': form.errors})
    else:
        form = DriverForm()
        return render(request, 'FormDriver.html', {'form': form})


def driversList(request):
    # دریافت تمام رانندگان
    drivers = Driver.objects.all()
    # دریافت فیلترهای ورودی
    city = request.GET.get('city', '').strip()
    date_filter = request.GET.get('date', '').strip()

    # فیلتر بر اساس شهر
    if city:
        drivers = drivers.filter(city=city)

    # فیلتر بر اساس تاریخ
    if date_filter == 'today':
        today = date.today()
        drivers = drivers.filter(date=today)
    elif date_filter == 'tomorrow':
        tomorrow = date.today() + timedelta(days=1)
        drivers = drivers.filter(date=tomorrow)

    return render(request, 'home.html', {'drivers': drivers})
