from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib  import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render (request, 'authenticate_home/home.html', {})

#login function
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

#Logout function
def logout_user(request):
    logout(request)
    messages.success(request,('You have logged out!'))
    return redirect('home')


def register_user(request):
    if request.method =='POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user = authenticate(request, username=username, password=password)
             login(request, user)
             messages.success(request,('Thank you for youregistration'))
             return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render (request, 'authenticate_home/register.html', context)