from django.contrib import admin
from django.urls import path
from .views import index,details

urlpatterns = [
    path("", index, name="home"),
    path("produtos/", details, name="details" )
]
