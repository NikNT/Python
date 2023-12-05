from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('This is Homepage')
    context = {
        'first_name' : 'Nikhil', 
        'last_name' : 'Tanwar'
    }
    messages.success(request, 'Test Message')
    return render(request,'index.html', context)

def about(request):
    # return HttpResponse('About Page')
    return render(request, 'about.html')

def services(request):
    # return HttpResponse('Services Page')
    return render(request, 'services.html')
    

def contact(request):
    # return HttpResponse('Contact Page')
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Message sent.")
    return render(request, 'contact.html')
    
    
