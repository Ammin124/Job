from django.shortcuts import render, redirect
from .models import Registeration
from django.urls import reverse
from .forms import RegisterationForm

# Create your views here.
def register(request):
    registerationForm = RegisterationForm()
    if request.POST:
        registerationForm = RegisterationForm(request.POST)
        if registerationForm.is_valid():
            registerationForm.save()
            return redirect(reverse('thank'))

    context ={
        "form": registerationForm,
    }
    return render(request, 'Auth/register.html',context)

def thank(request):
    return render(request,'Auth/thank.html')