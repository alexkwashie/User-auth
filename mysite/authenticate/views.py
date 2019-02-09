from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout, update_session_auth_hash
from django.contrib  import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm # from form.py
from .forms  import editProfileForm

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
         form = SignUpForm(request.POST) #use this to allow user sign up form
         if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user = authenticate(request, username=username, password=password)
             login(request, user)
             messages.success(request,('Thank you for you registration'))
             return redirect('home')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render (request, 'authenticate_home/register.html', context)

def edit_profile(request):
    if request.method =='POST':
         form = editProfileForm(request.POST, instance = request.user) #use this to allow changing form
         if form.is_valid():
             form.save()
             messages.success(request,('Thank you, Your details have been amended'))
             return redirect('home')

    else:
        form = editProfileForm(instance = request.user) #use this to allow changing form

    context = {'form': form}
    return render (request, 'authenticate_home/edit_profile.html', context)


def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data = request.POST,user = request.user) #use 'data' here to request post
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)#use this to prevent it from login user out
            messages.success(request,('Thank you, Your details have been amended'))
            return redirect('home')

    else:
        form = PasswordChangeForm(user = request.user) #use this to allow changing form

    context = {'form': form}
    return render (request, 'authenticate_home/change_password.html', context)