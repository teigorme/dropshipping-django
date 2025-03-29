from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            query = User.objects.get(email=email)
            user = authenticate(request, username=query.username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                messages.error(
                    request,
                    "Credenciais inválidas. Verifique seu e-mail ou palavra-passe.",
                )

    return render(request, "auth/login.html", status=200, context={"form": form})


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

           
            if User.objects.filter(email=email).exists():
                messages.error(
                    request,
                    "Este e-mail já está registrado.Tente novamente com outro e-mail",
                )
            
            elif confirm_password != password:
                messages.error(request, "A palavra-passe de confirmação não é igual a palavra-passe.Tente novamente")
            else:

                User.objects.create(
                    username=username,
                    email=email,
                    password=make_password(password),
                )
                messages.success(request, "Sua conta foi criada com sucesso!")
                return redirect("login")

    return render(request, "auth/register.html", status=200, context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")



def index(request):
    products = Product.objects.all()[:4]
    context = {"products":products}
    return render(request, "index.html",context=context)

def products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "products.html",context=context)

def details(request,id):
    product = get_object_or_404(Product, id=id) 
    return render(request, "details.html", {"product": product})

