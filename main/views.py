from datetime import datetime
from pstats import Stats
from django.shortcuts import render,HttpResponse
from datetime import datetime
from main.models import Contact
from django.contrib import messages
import mimetypes

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, number=number , email=email , desc = desc , date=datetime.today())
        contact.save()
        messages.add_message(request, messages.INFO, 'Congratulations!!..Your feedback is submitted successfully')
    return render(request,'contact.html')


def download(request):

    return render(request, 'resume.html')