from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Tasktodo
# Create your views here.

#create home function
def home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        new_todo = Tasktodo(user=request.user,todo_name = task)                                              
    return render(request,"TasktodoApp/Tasktodo.html", {})

#create register function
def register(request):
    if request.method == "POST":                                    # Checks if request that is sent is POST
        username = request.POST.get("username")                     # Gets the username, from the form, using id of the buttom 
        email = request.POST.get("email")                           # Gets the email
        password = request.POST.get("password")                     # Gets the password
        
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect("register")
        
        get_all_usernames = User.objects.filter(username)

        if get_all_usernames:
            messages.error(request,"That username already exists, use a different one.")
            return redirect("register")

        new_user = User.objects.create_user(username,email,password)    # Create a user
        new_user.save()                                                 # Save user
    return render(request,"TasktodoApp/register.html", {})

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect("home-page")
        else:
            messages.error(request,"Wrong login details or user does not exist.\
                            Try to log in again.")
            return redirect("login")

    return render(request,"TasktodoApp/login.html", {})