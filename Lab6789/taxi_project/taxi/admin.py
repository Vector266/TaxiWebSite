from django.contrib import admin
from .models import User, Client, Driver, Car, Route, Trip

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'plate_number', 'driver')

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('client', 'driver', 'start_time', 'end_time', 'distance_km', 'cost')
    filter_horizontal = ('routes',)
