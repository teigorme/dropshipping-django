from django.shortcuts import render


def login(request):
    return render(request, "auth/login.html")

def register(request):
    return render(request, "auth/register.html")


def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def details(request,id):
    return render(request, "details.html")

