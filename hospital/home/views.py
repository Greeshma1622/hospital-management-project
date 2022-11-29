from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def Doctor(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def Department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'departments.html', dict_dept)

def contact(request):
    return render(request,'contact.html')
