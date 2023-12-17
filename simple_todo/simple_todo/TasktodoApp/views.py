from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"TasktodoApp/Tasktodo.html", {})

def register(request):
    return render(request,"TasktodoApp/register.html", {})

def loginpage(request):
    return render(request,"TasktodoApp/login.html", {})