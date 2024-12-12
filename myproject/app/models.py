from django.db import models


# models.py
class Driver(models.Model):
    username = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    route = models.CharField(max_length=100, blank=True, null=True)  # مسیر راننده
    image = models.ImageField(upload_to='images/' , null=True, blank=True)
    vehicle_type = models.CharField(max_length=100, null=True)  # نوع ماشین
    vehicle_model = models.CharField(max_length=100, null=True)  # مدل ماشین
    city = models.CharField(max_length=100)
    date = models.DateField()  # فیلد تاریخ
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class people(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
