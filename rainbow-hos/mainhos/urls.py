from django.urls import path
from . import views 



urlpatterns = [
    path('',views.home_view,name = 'homepage'),
    path('doctors', views.ViewDoctors.as_view(), name='view_doctors'),
    path('doctors/<int:pk>', views.DoctorDetailView.as_view(), name = 'doc_details'),
    path('doctors/edit/<int:pk>', views.DoctorEditView.as_view(), name = 'doc_edit'),
    path('doctors/add/', views.AddDoctor.as_view(), name='add_doctor'),
    path('appointment/add',views.AddAppointment.as_view(), name='patient'),
    # path('patients/edit/<int:pk>',views.PatientEditView.as_view(), name='edit_patient'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('staff/', views.staff_list, name='staff_list'),
    path('appointment/book/', views.book_appointment, name='book_appointment'),
    path('appointments/pending/', views.PendingAppointments.as_view(), name='pending_appointments'),

    
]
