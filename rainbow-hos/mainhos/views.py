
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from .models import Doctor
from .forms import HospitalStaffForm
from .models import HospitalStaff
import razorpay
from django.http import JsonResponse

from django.conf import settings


client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))




def home_view(request):
    return render(request, 'home.html')


class AddDoctor(CreateView):
    model = Doctor
    template_name = 'add_doctor.html'
    fields = "__all__"
    success_url = '/'

class ViewDoctors(ListView):
    model = Doctor
    template_name = 'view_doctors.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'doctor_details.html'

class DoctorEditView(UpdateView):
    model = Doctor 
    fields = '__all__'
    template_name = 'doc_edit.html'
    success_url = '/'








def add_staff(request):
    if request.method == 'POST':
        form = HospitalStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = HospitalStaffForm()
    return render(request, 'add_staff.html', {'form': form})

def staff_list(request):
    staff = HospitalStaff.objects.all()
    return render(request, 'staff_list.html', {'staff': staff})




 


 