from django.contrib import admin
from django.urls import path
from .views import index,details,login,register,products

urlpatterns = [
    path("", index, name="home"),
    path("produtos/", products, name="products" ),
    path("produtos/<int:id>", details, name="details" ),
    path("entrar/", login, name="login" ),
    path("registar-se/", register, name="register" ),
]
