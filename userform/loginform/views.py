from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.models import User
from django.db import IntegrityError  


def signup(request):
    if request.method =="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                save_user=User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
                save_user.save()
                return render(request,'signup.html',{'form':UserCreationForm(),'info':'The user '+request.POST.get('username')+' has been registered'})
            except IntegrityError: 
                return render(request,'signup.html',{'form':UserCreationForm(),'error':'The user '+request.POST.get('username')+' already exist'})
        else:
            return render(request,'signup.html',{'form':UserCreationForm(),'error':'The password has not matched'})
    else:
        return render(request,'signup.html',{'form':UserCreationForm})
