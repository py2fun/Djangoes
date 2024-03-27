from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import PostModelForm

# Create your views here.

def index(request):
    user = User.objects.create_user(username="Ulrich",email="ulrich@gmail.com",password="mac12")
    user.save()
    return render(request,'first_app/index.html')

def home(request):
    return HttpResponse("Welcome to home page!")

def pytip(request):
    return HttpResponse("Welcome to pytip page!")

def forms(request):
    form = PostModelForm( request.POST or None)
    data = "None"
    text= "None"
    if form.is_valid():
        data = form.cleaned_data
        text= form.cleaned_data.get("text")
    return render(request,'first_app/forms.html', {'form': form,'data': data, 'text': text})