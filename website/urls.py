from django.contrib import admin
from django.urls import path
from .views import index,details,login,register,products,logout_view

urlpatterns = [
    path("", index, name="home"),
    path("produtos/", products, name="products" ),
    path("produtos/<int:id>", details, name="details" ),
    path("entrar/", login, name="login" ),
    path("registar-se/", register, name="register" ),
     path("sair-da-conta/", logout_view, name="logout" ),

]
