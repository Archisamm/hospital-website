from django.shortcuts import render
from django.views.generic import CreateView
from .models import Patient
from django.urls import reverse_lazy

# Create your views here.
class AddPatient(CreateView):
    model = Patient
    fields = '__all__'
    success_url = '/'    


from .forms import CustomRegisterForm

class UserRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin') 

from.forms import CustomLoginForm
from django.contrib.auth.views import LoginView

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLoginForm
