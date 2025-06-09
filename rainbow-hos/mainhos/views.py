
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from .models import Doctor, Appointment
from .forms import HospitalStaffForm
from .models import HospitalStaff
import razorpay
from django.http import JsonResponse
from .forms import AppointmentForm
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

class AddAppointment(CreateView):
    model = Appointment
    template_name = 'appointment.html'
    success_url = '/'
    fields = ['doctor', 'patient', 'app_date' , 'advance_fee','payment_status']

def addAppointments(request, doctor_id):
    app = Appointment.objects.create()


class ViewAppointment(ListView):
    model = Appointment
    template_name = 'view_appointments.html'
    context_object_name = 'appointments'
    fields = '__all__'


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST,user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.is_paid = False
            appointment.save()

            
            payment = client.order.create({
                'amount': int(appointment.advance_fee * 100),
                'currency': 'INR',
                'payment_capture': '1'
            })

            appointment.payment_id = payment['id']
            appointment.save()

            context = {
                'appointment': appointment,
                'payment': payment,
                'razorpay_key': settings.RAZORPAY_KEY_ID
            }
            return render(request, 'payment.html', context)
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})



@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(patient__user=request.user)
    return render(request, 'my_appointments.html', {'appointments': appointments})

  
        
    
        
class PendingAppointments(ListView):
    model = Appointment
    template_name = 'pending_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(status='pending')






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




 


 