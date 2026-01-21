from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("home")

def register_views(request):
    return HttpResponse("register")

def login_views(request):
    return HttpResponse("login")

def logout_views(request):
    return HttpResponse("logout")

def delete_task(request):
    return HttpResponse("deleted")

