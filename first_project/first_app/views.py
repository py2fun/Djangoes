from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def home(request):
    return HttpResponse("Welcome to home page!")

def pytip(request):
    return HttpResponse("Welcome to pytip page!")

def forms(request):
    form = SearchForm()
    return render(request,'first_app/forms.html', {'form': form})