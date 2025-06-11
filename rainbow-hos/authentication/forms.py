from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import ModelForm
from .models import Patient

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control x',
            'placeholder' : 'Enter your username',
            
        })
    )

    password1 = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        })
    )

    class Meta:
        model = User 
        fields = ('username','password1','password2')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your username'
        })
    )

    password = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ['user']
        widgets = {
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
        }