from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= {
        "variable": "this is sent"
        "variable1" "My name is Gaurav"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")
def service(request):
    return render(request, 'service.html')
    # return HttpResponse("this is service page")
def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        additionaldetails = request.POST.get('additionaldetails')
        contact = Contact(name= name, email=email, phone=phone, additionaldetails=additionaldetails, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")