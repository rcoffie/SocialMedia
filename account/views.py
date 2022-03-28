from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.
def dashboard(request):

  return render(request,'account/dashboard.html')

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'user created')
      return redirect('account:login')
  else:
    form = SignUpForm()
  return render(request, 'account/signup.html',{
    'form':form,
  })


def userlogin(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f'you are not logged in as {username},')
        return redirect('account:dashboard')
      else:
        messages.error(request,'invalid user credentials')
    else:
      messages.error(request, "invalid credntials 2")
  form = AuthenticationForm()
  return render(request, 'account/login.html',{
    'form':form,
  })
