from django.db import models

from authentication.models import Patient
from django.core.exceptions import ValidationError
from django.utils import timezone



class Doctor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='doctors/', null=True)
    dob = models.DateField()
    gender = models.CharField(choices=[
        ('m','male'),('f','female'), ('o','others')
    ])
    booking_amount = models.PositiveBigIntegerField(default=500)
    phno_pin = models.CharField(choices=[
    ('+1', '🇺🇸 United States (+1)'),
    ('+44', '🇬🇧 United Kingdom (+44)'),
    ('+91', '🇮🇳 India (+91)'),
    ('+61', '🇦🇺 Australia (+61)'),
    ('+81', '🇯🇵 Japan (+81)'),
    ('+49', '🇩🇪 Germany (+49)'),
    ('+33', '🇫🇷 France (+33)'),
    ('+39', '🇮🇹 Italy (+39)'),
    ('+86', '🇨🇳 China (+86)'),
    ('+7', '🇷🇺 Russia (+7)'),
    ('+34', '🇪🇸 Spain (+34)'),
    ('+971', '🇦🇪 UAE (+971)'),
    ('+92', '🇵🇰 Pakistan (+92)'),
    ('+880', '🇧🇩 Bangladesh (+880)'),
    ('+55', '🇧🇷 Brazil (+55)'),
    ('+27', '🇿🇦 South Africa (+27)'),
    ('+82', '🇰🇷 South Korea (+82)'),
    ('+62', '🇮🇩 Indonesia (+62)'),
    ('+20', '🇪🇬 Egypt (+20)'),
    ('+234', '🇳🇬 Nigeria (+234)'),
    ('+66', '🇹🇭 Thailand (+66)'),
    ('+63', '🇵🇭 Philippines (+63)'),
    ('+98', '🇮🇷 Iran (+98)'),
    ('+964', '🇮🇶 Iraq (+964)'),
    ('+964', '🇸🇦 Saudi Arabia (+966)'),
    ('+972', '🇮🇱 Israel (+972)'),
    ('+212', '🇲🇦 Morocco (+212)'),
    ('+60', '🇲🇾 Malaysia (+60)'),
    ('+46', '🇸🇪 Sweden (+46)'),
    ('+358', '🇫🇮 Finland (+358)'),
    ('+47', '🇳🇴 Norway (+47)'),
    ('+41', '🇨🇭 Switzerland (+41)'),
    ('+90', '🇹🇷 Turkey (+90)'),
    ('+84', '🇻🇳 Vietnam (+84)'),
    ('+351', '🇵🇹 Portugal (+351)'),
    ('+48', '🇵🇱 Poland (+48)'),
    ('+52', '🇲🇽 Mexico (+52)'),
    ('+64', '🇳🇿 New Zealand (+64)'),
    ('+31', '🇳🇱 Netherlands (+31)'),
    ('+43', '🇦🇹 Austria (+43)'),
    ('+1-268', '🇦🇬 Antigua and Barbuda (+1-268)'),
    ('+1-242', '🇧🇸 Bahamas (+1-242)'),
    ('+1-246', '🇧🇧 Barbados (+1-246)'),
    ('+1-784', '🇻🇨 Saint Vincent (+1-784)'),
    ('+1-758', '🇱🇨 Saint Lucia (+1-758)'),
    ('+1-868', '🇹🇹 Trinidad & Tobago (+1-868)'),
], max_length=8)
    phno = models.CharField(max_length=10)
    category = models.CharField(choices=[
    ('general', 'General Physician'),
    ('cardiologist', 'Cardiologist'),
    ('dermatologist', 'Dermatologist'),
    ('neurologist', 'Neurologist'),
    ('orthopedic', 'Orthopedic Surgeon'),
    ('pediatrician', 'Pediatrician'),
    ('gynecologist', 'Gynecologist'),
    ('psychiatrist', 'Psychiatrist'),
    ('ent', 'ENT Specialist'),
    ('oncologist', 'Oncologist'),
    ('urologist', 'Urologist'),
    ('gastroenterologist', 'Gastroenterologist'),
    ('pulmonologist', 'Pulmonologist'),
    ('radiologist', 'Radiologist'),
    ('anesthesiologist', 'Anesthesiologist'),
    ('nephrologist', 'Nephrologist'),
    ('endocrinologist', 'Endocrinologist'),
    ('surgeon', 'General Surgeon'),
    ('other', 'Other'),
    ], max_length=30)

    def __str__(self):
        return f"Dr. {self.name}"





class HospitalStaff(models.Model):
    STAFF_ROLES = [
        ('admin', 'Administrator'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Receptionist'),
        ('lab', 'Lab Technician'),
        ('janitor', 'Janitor'),
        ('other', 'Other'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    role = models.CharField(max_length=50, choices=STAFF_ROLES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_joined = models.DateField(auto_now_add=True)
    # pincode = models.CharField(max_length=6)
    # image = models.ImageField(upload_to='staff/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"
