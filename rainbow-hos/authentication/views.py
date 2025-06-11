from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PatientForm,  CustomRegisterForm, PatientForm

from django.contrib import messages
from django.core.exceptions import ValidationError 


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
# class AddPatient(CreateView):
#     model = Patient
#     fields = '__all__'
#     success_url = '/'    
#     template_name = 'add_patient_form.html'



class UserRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin') 

from.forms import CustomLoginForm
from django.contrib.auth.views import LoginView

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLoginForm




@login_required
def addPatient(request):
    template_name = 'add_patient_form.html'

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Set user from request
            try:
                patient.full_clean()  # Explicitly run model validation
                patient.save()
                messages.success(request, "Patient added successfully.")
                return redirect('homepage')  
            except ValidationError as e:
                # Add error messages to the form
                for field, errors in e.message_dict.items():
                    for error in errors:
                        form.add_error(field, error)
    else:
        form = PatientForm()

    context = {'form': form}
    return render(request, template_name, context)
