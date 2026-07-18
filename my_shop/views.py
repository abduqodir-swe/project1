# Importer
from django.shortcuts import render

def home(request):
    return render(request, "my_shop/index.html")

def about(request):
    return render(request, "my_shop/about.html")

def contact(request):
    return render(request, "my_shop/contact.html")