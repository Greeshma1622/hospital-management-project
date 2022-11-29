from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('About', views.About,name='About'),
    path('Booking', views.Booking,name='Booking'),
    path('Doctors', views.Doctor,name='Doctors'),
    path('Departments', views.Department,name='Departments'),
    path('Contact', views.contact,name='Contact'),
]