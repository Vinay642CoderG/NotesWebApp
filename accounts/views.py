from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import MyUser
# Create your views here.

def userLogin(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        data=request.POST
        email=data.get('email')
        password=data.get('password')
        user=authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            if MyUser.objects.filter(email__contains=email).exists():
                messages.error(request, "Wrong Password!")
            else:
                messages.error(request, "Wrong User Credentials!")
            return redirect('login')
    return render(request, 'login.html')

def userSignup(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        data=request.POST
        formFields = {
            'first_name':data.get('first_name'),
            'last_name':data.get('last_name'),
            'email':data.get('email'),
            'password':data.get('password'),
        }
        user, _created = MyUser.objects.get_or_create(**formFields)
        if _created:
            user.set_password(formFields['password'])
            user.save()
            messages.success(request, "User created!")
            return redirect('login')
        else:
            messages.error(request, "User not created!")
            return redirect('signup')
    return render(request, 'signup.html')


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout successful!")
        return redirect('login')
    else:
        return redirect('index')