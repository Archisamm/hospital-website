from django.db import models
from authentication.models import Patient
from django.core.exceptions import ValidationError
from django.utils import timezone
from mainhos.models import Doctor
from django.contrib.auth.models import User
# Create your models here.



class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval. Please wait...'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
        ('rescheduled', 'Rescheduled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    app_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,default='pending', max_length=20)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True)
    advance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)

    @property
    def total_amount(self):
        if self.doctor:
            return int(self.doctor.booking_amount)
        else:
            return int(500)
    # def clean(self):
    #     super().clean()

    #     # 1. Appointment date must be in the future
    #     if self.app_date and self.date_created and self.app_date <= self.date_created:   
    #         raise ValidationError("Appointment date must be in the future.")

    #     # 2. Prevent double booking of the doctor at the same time
    #     if self.app_date and self.doctor:
    #         overlapping = Appointment.objects.filter(
    #             doctor=self.doctor,
    #             app_date=self.app_date,
                
    #         )
    #         if self.pk:
    #             overlapping = overlapping.exclude(pk=self.pk)

    #         if overlapping.exists():
    #             raise ValidationError("This doctor already has an appointment at the selected time.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validates before saving
        super().save(*args, **kwargs)

    def __str__(self):
        patient_name = getattr(self.patient, 'name', 'Unknown')
        doctor_name = getattr(self.doctor, 'name', 'Unknown')
        date_str = self.app_date.strftime('%Y-%m-%d %H:%M') if self.app_date else 'Unknown'
        return f"{patient_name} with Dr. {doctor_name} on {date_str}"
    


