from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    return render(request,"index.html",)

def about(request):
    # return HttpResponse("This is AboutPage")
    return render(request,"about.html",)


def contact(request):
    return render(request,"contact.html",)


def icecream(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        

    return render(request,"icecream.html",)

def vegHome(request):
    return render(request,"vegHome.html",)