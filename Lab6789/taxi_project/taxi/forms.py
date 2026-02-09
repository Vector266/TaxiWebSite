from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Trip

class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label="Роль")

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
