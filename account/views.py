from django.shortcuts import render
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.utils import timezone
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required

def signupfunc(request):
    return render(request, 'signup.html')
