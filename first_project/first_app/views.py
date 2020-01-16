from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def home(request):
    return HttpResponse("Welcome to home page!")

def educative(request):
    return HttpResponse("Welcome to Educative page!")