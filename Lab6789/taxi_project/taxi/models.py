from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Клиент'),
        ('dispatcher', 'Диспетчер'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Driver(models.Model):
    name = models.CharField("Имя водителя", max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    model = models.CharField("Модель", max_length=100)
    plate_number = models.CharField("Номерной знак", max_length=20)

    def __str__(self):
        return f"{self.model} ({self.plate_number})"

class Route(models.Model):
    name = models.CharField("Название маршрута", max_length=200)

    def __str__(self):
        return self.name

class Trip(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start_time = models.DateTimeField("Время начала поездки")
    end_time = models.DateTimeField("Время окончания поездки")
    distance_km = models.FloatField("Дистанция (км)")
    cost = models.DecimalField("Стоимость", max_digits=8, decimal_places=2)
    routes = models.ManyToManyField(Route)

    def __str__(self):
        return f"Поездка {self.client} с {self.driver} {self.start_time.date()}"
