from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .forms import AppointmentForm
from .models import Doctor, Appointment

# Create your views here.
def payment_success(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        try:
            appointment = Appointment.objects.get(payment_id=request.POST.get('razorpay_order_id'))
            appointment.is_paid = True
            appointment.payment_status = True  # fix field name
            appointment.status = 'scheduled'
            appointment.save()
            return render(request, 'success.html', {'appointment': appointment})
        except Appointment.DoesNotExist:
            return HttpResponse("Invalid payment/order ID.")
    else:
        return redirect('homepage')  # Add this return to avoid returning None
