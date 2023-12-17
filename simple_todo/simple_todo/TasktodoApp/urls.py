from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home-page"),             #Add path to home page
    path("register/", views.register, name="register"), #Add path to register page
    path("login/",views.loginpage, name = "login")      #Add path to login page
]