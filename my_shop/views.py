# Importer
from django.shortcuts import render

def home(request):
    context = {
        "username" : "Ali",
        "is_admin" : False,
        "students" : [
            {"name": "Vali", "score": 90},
            {"name": "Sardor", "score": 82},
            {"name": "Jamshid", "score": 65},
            {"name": "Malika", "score": 45},
        ]
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

def blog(request):
    context = {
        "title" : "Blog"
    }
    return render(request, "my_shop/blog.html", context)
