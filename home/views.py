from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index-4.html')

def appointment(request):
    return render(request,'appointment.html')
