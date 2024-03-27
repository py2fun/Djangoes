from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home/',views.home,name="home"),
    path('pytip/',views.pytip,name="educative"),
    path('forms/',views.forms,name="form"),
]