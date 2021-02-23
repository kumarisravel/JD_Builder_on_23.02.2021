from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.

def register(request):
    user_creation_form=UserCreationForm()
    return render(request,'account/register.html',{'user_form':user_creation_form})
