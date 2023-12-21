from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home-page"),             #Add path to home page
    path("register/", views.register, name="register"), #Add path to register page
    path("login/", views.loginpage, name = "login"),      #Add path to login
    path("logout/", views.logout_user, name = "logout"),
    path("update_task_order/", views.update_task_order, name ="update_task_order"), 
    path("delete_task/<str:name>/", views.delete_task, name = "delete"),
    path("update/<str:name>/", views.update, name = "update"),
    
]