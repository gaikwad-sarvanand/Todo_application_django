from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!")
            return redirect("todo:index")
        messages.error(request, "Unsuccessful Registration!")
    form = RegistrationForm()
    return render(request, "register.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"Your are now logged in as {username}")
            return redirect("todo:add_todo")
        else:
            messages.error(request, "Invalid username and password")
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, f"Logged out successfully!")
    return redirect("todo:index")
