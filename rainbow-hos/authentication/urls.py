from django.urls import path
from . import views
from.views import UserRegister,UserLogin



urlpatterns = [
    path('patients/', views.AddPatient.as_view(), name = 'patients'),
    path('register/',UserRegister.as_view(),name='signup'),
    path('signin/',UserLogin.as_view(),name='signin'),
]
