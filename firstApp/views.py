from datetime import timedelta, timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm, LoginForm
# from .models import AuthToken
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token

CONTACT_DATA = {}

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(form.cleaned_data['password'])
            user.save()

            Token.objects.create(user=user)
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'firstApp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, created= Token.objects.get_or_create(user=user)
            response = redirect('home')
            response.set_cookie('auth_token', token.key, max_age=3600)  # 1 hour
            return response 
        else:
             return render(request, 'firstApp/login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request, 'firstApp/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect(reverse('login'))


def home(request):
    return render(request, 'firstApp/home.html')

def contact(request):
    global CONTACT_DATA
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print("RAN")
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(f"Subject: {subject}, Email: {email}, Message: {message}")
            CONTACT_DATA = {
                'subject': subject,
                'email': email,
                'message': message
            }
            return HttpResponseRedirect(reverse('contact_success'))
    else:
        form = ContactForm()
    return render(request, 'firstApp/contact.html', {'form': form})

def contact_success(request):
    global CONTACT_DATA
    if CONTACT_DATA:
        contact_data = CONTACT_DATA
        
        CONTACT_DATA = {}
        return render(request, 'firstApp/contact_success.html', contact_data)
    else:
        return HttpResponse("Invalid access to success page.", status=400)

def about(request):
    return render(request, 'firstApp/about.html')
