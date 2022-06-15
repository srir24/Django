from django.shortcuts import render
from crud_op.models import stud
from django.contrib import messages
# Create your views here.

def display(request):
    res=stud.objects.all()
    return render(request,"index.html",{'stud':res})
def add(request):
    if request.method=="POST":
        if request.POST.get('sname') and request.POST.get('semail') and request.POST.get('saddress') and request.POST.get('smobile') and request.POST.get('sgender'):
            stud_obj=stud()
            stud_obj.sname=request.POST.get('sname')
            stud_obj.semail=request.POST.get('semail')
            stud_obj.saddress=request.POST.get('saddress')
            stud_obj.smobile=request.POST.get('smobile') 
            stud_obj.sgender=request.POST.get('sgender')
            stud_obj.save()
            messages.success(request," The record "+ stud_obj.sname + "has been inserted successfully")
            return render(request,"create.html")
    else:
        return render(request,"create.html")
def edit(request, id):
    getdetails=stud.objects.get(id=id)
    return render(request,"edit.html",{'stud':getdetails})