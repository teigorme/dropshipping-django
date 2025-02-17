from django.shortcuts import render


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")

def details(request):
    return render(request, "details.html")
