from django.shortcuts import render
from django.http import HttpResponse

from .forms import TestForm

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def home(request):
    return HttpResponse("Welcome to home page!")

def pytip(request):
    return HttpResponse("Welcome to pytip page!")

def forms(request):
    inital_dict={
        "text": "Some initial data",
        "integer": 123,
    }
    form = TestForm( request.POST or None,initial=inital_dict)
    data = "None"
    text= "None"
    if form.is_valid():
        data = form.cleaned_data
        text= form.cleaned_data.get("text")
    return render(request,'first_app/forms.html', {'form': form,'data': data, 'text': text})