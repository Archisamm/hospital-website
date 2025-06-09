from django import forms
from .models import HospitalStaff
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['app_date', 'status', 'advance_fee']
    widgets = {
            'appointment_date': forms.DateTimeInput(attrs={
                'placeholder': 'dd-mm-yyyy hh:mm AM/PM',
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select status'
            }),
            'advance_fee': forms.NumberInput(attrs={
                'placeholder': 'Enter total amount in ₹',
                'class': 'form-control'
            }),
        }
class HospitalStaffForm(forms.ModelForm):
    class Meta:
        model = HospitalStaff
        fields = '__all__'
    