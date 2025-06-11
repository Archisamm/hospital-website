from django import forms
from .models import HospitalStaff

class HospitalStaffForm(forms.ModelForm):
    class Meta:
        model = HospitalStaff
        fields = '__all__'
    