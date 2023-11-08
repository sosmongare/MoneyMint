from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
# Create your views here.

# render index.html
def index(request):
    return render(request, 'authentication/login.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: #  creates a new instance of UserCreationForm and renders the 'signup.html' template, passing the form as context.
        form = UserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')