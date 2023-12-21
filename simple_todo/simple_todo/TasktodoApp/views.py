from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Tasktodo
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
# Create your views here.

#create home function
@login_required
@login_required
def home(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            new_todo = Tasktodo(user=request.user, todo_name=task)
            new_todo.save()
            return redirect(reverse("home-page"))

    # Retrieve tasks in the correct order based on the order_index field
    all_todos = Tasktodo.objects.filter(user=request.user).order_by('order_index')

    context = {'todos': all_todos}
    return render(request, "TasktodoApp/Tasktodo.html", context)

#create register function
def register(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    
    if request.method == "POST":                                    # Checks if request that is sent is POST
        username = request.POST.get("username")                     # Gets the username, from the form, using id of the buttom 
        email = request.POST.get("email")                           # Gets the email
        password = request.POST.get("password")                     # Gets the password
        
        if len(password) < 8:
            messages.error(request, "Password must be consist of at least 8 characters.")
            return redirect("register")
        
        get_all_usernames = User.objects.filter(username)

        if get_all_usernames:
            messages.error(request,"That username already exists, use a different one.")
            return redirect("register")

        new_user = User.objects.create_user(username,email,password)    # Create a user
        new_user.save()                                                 # Save user
    return render(request,"TasktodoApp/register.html", {})


def loginpage(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    
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


def logout_user(request):
    logout(request)
    return redirect("login")


@csrf_exempt
def update_task_order(request):
    if request.method == "POST":
        new_order = request.POST.get('new_order').split(',')
        try:
            with transaction.atomic():
                # Iterate over the received order and update the order_index for each task
                for index, todo_id in enumerate(new_order):
                    task = Tasktodo.objects.get(id=todo_id, user=request.user)
                    task.order_index = index
                    task.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




def delete_task(request,name):
    get_todo = Tasktodo.objects.get(user=request.user, todo_name=name)
    get_todo.delete()
    return redirect("home-page")


def update(request,name):
    get_todo = Tasktodo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect("home-page")
