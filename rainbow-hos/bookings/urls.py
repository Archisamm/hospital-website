from django.urls import path
from.views import render
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('book/<int:doctor_id>', views.book_appointment, name='book_appointment'),  # Function-based
    # path('book/', views.BookAppointmentView.as_view(), name='book_appointment'),  # Class-based
    # path('success/', lambda request: render(request, 'success.html'), name='appointment_success'),
    
    # path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('success/', views.appointment_success, name='appointment_success'),
    path('appointments/', views.ViewAppointment.as_view(), name='view_appointments'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('pending-appointments/', views.PendingAppointments.as_view(), name='pending_appointments')
]
