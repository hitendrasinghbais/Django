from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World. You are at Home page")
    return render(request,'website/index.html')

def about(request):
    #return HttpResponse("Now you are at about page")
    return render(request,'website/about.html')

def contact(request):
   #return HttpResponse("Hello world. You are at contact page")
   return render(request,'website/contact.html')