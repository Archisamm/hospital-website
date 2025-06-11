from django.shortcuts import render
from .models import Appointment
from django.views.generic import CreateView, ListView
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import AppointmentForm
from mainhos.models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from bookings.models import Appointment


@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = AppointmentForm(user=request.user, data=request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.user = request.user
            appointment.patient = form.cleaned_data['patient']
            appointment.full_clean()  # Triggers model validation with doctor set
            appointment.save()

            # Redirect to Razorpay
            payment_url = reverse('payment:create_razorpay_order', args=[appointment.id])
            return redirect(payment_url)
    else:
        form = AppointmentForm(user=request.user)

    return render(request, 'book_appointment.html', {
        'form': form,
        'doctor': doctor,
        'show_add_patient': True,
    })




class ViewAppointment(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(patient__user=self.request.user)




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


def appointment_success(request):
    
    return render(request, 'success.html')