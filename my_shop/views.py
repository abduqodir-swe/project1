# Importer
from django.shortcuts import render

def home(request):
    context = {
        "title" : "Main"
    }
    return render(request, "my_shop/index.html", context)

def about(request):
    context = {
        "title" : "About"
    }
    return render(request, "my_shop/about.html", context)

def contact(request):
    context = {
        "phone" : "+998901231231"
    }
    return render(request, "my_shop/contact.html", context)