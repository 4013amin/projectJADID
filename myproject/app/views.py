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


from .models import Driver
from django.shortcuts import render
from datetime import date, timedelta

from .models import Driver
from django.shortcuts import render
from datetime import date, timedelta

def driversList(request):
    # دریافت تمامی رانندگان
    drivers = Driver.objects.all()

    # دریافت فیلترها از ورودی کاربر
    city = request.GET.get('city', '').strip()  # فیلتر بر اساس شهر
    date_filter = request.GET.get('date', '').strip()  # فیلتر بر اساس تاریخ

    # اعمال فیلتر شهر
    if city:
        drivers = drivers.filter(route__icontains=city)  # جستجو در مسیر راننده

    # اعمال فیلتر تاریخ
    if date_filter == 'today':
        today = date.today()
        drivers = drivers.filter(date=today)
    elif date_filter == 'tomorrow':
        tomorrow = date.today() + timedelta(days=1)
        drivers = drivers.filter(date=tomorrow)

    # اطلاعات اضافی مانند آخرین رانندگان اضافه‌شده
    latest_drivers = Driver.objects.order_by('-date')[:5]

    return render(request, 'home.html', {
        'drivers': drivers,
        'latest_drivers': latest_drivers,
        'city': city,
        'date_filter': date_filter
    })

