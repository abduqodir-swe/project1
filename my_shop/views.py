from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def about(request):
    return HttpResponse("<h1>About Us Page</h1>")

def contact(request):
    return HttpResponse("<h1>+998901234567</h1>")

    