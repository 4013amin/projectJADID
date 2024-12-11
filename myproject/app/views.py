from django.shortcuts import render

from .forms import DriverForm
from .models import Driver


def index(request):
    drivers = Driver.objects.filter(approved=True)
    return render(request, 'home.html', {'drivers': drivers})


from django.shortcuts import render
from .forms import DriverForm


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
