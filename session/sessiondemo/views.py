from django.shortcuts import render
from django.http import HttpResponse  
# Create your views here.


def setsession(request):  
        request.session['name'] = 'Surya'  
        request.session['email'] = 'surya.thesun@gmail.com'  
        return HttpResponse("session is set")  



def getsession(request):  
        sname = request.session['name']  
        semail = request.session['email']  
        return HttpResponse(sname+" "+semail);  


def setcookie(request):  
    response = HttpResponse("Cookie is set")  
    response.set_cookie('cookie_key', 'Hello I am cookie')  
    return response  

def getcookie(request):  
    tutorial  = request.COOKIES['cookie_key']  
    return HttpResponse("Saved Cookie details: "+  tutorial); 