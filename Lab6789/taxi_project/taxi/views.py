from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistrationForm, TripForm
from .models import Trip

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trip_list')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import authenticate, login
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('trip_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def is_dispatcher(user):
    return user.is_authenticated and user.role == 'dispatcher'

@login_required
@user_passes_test(is_dispatcher)
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trip_list.html', {'trips': trips})

@login_required
@user_passes_test(is_dispatcher)
def trip_create(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'trip_form.html', {'form': form, 'title': 'Добавить поездку'})

@login_required
@user_passes_test(is_dispatcher)
def trip_update(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trip_form.html', {'form': form, 'title': 'Редактировать поездку'})

@login_required
@user_passes_test(is_dispatcher)
def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    return render(request, 'trip_confirm_delete.html', {'trip': trip})
