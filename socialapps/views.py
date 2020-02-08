from django.shortcuts import render, redirect
from .management.commands.dataload import Command
from .models import Item, MyPosts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def home(request):
    command = Command()
    item = Item.objects.all()
    command.handle()
    return render(request, "socialapps/home.html", {'item':item})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, "socialapps/signup.html", {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('main_view')
    else:
        form = AuthenticationForm()
    return render(request, 'socialapps/login.html', {'form':form})

def main_view(request):
    return render(request, 'socialapps/mainview.html')

def fb(request):
    command = Command()
    item = Item.objects.all()
    myPosts = MyPosts.objects.all()
    command.handle()
    return render(request, 'socialapps/fb.html', {'item':item, 'myPosts':myPosts})
