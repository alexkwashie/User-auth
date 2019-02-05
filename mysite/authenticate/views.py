from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib  import messages

# Create your views here.
def home(request):
    return render (request, 'authenticate_home/home.html', {})

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Yay!, You are logged in'))
            return redirect('home')
        else:
            messages.success(request,('Login Error'))
            return redirect('login')

    else:
        return render (request, 'authenticate_home/login.html', {})

