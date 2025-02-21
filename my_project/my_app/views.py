from django.shortcuts import render, HttpResponse
from datetime import datetime
from my_app.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    #logic to store data in database
    if request.method =='POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = datetime.today() #to get current date
        contact = Contact(full_name=full_name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!, We will get back to you soon.')

    return render(request, 'contact.html')

