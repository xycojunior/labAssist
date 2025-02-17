from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from GeralUtilits import *

from .forms import *
from .models import *

# Create your views here.
class Redirect(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_staff:
                return redirect('home_admin')
            else:
                return redirect('home')
        else:
            return redirect('landing_page')

class Login(View):
    def get(self, request):
        form = AuthenticationForm()

        context = {
            'form' : form
        }

        return render(request, 'authentication/login.html', context)
    
    def post(self, request):
        data = request.POST.copy()
        data['username'] = data['username'].lower()

        form = AuthenticationForm(request, data = data)

        errors = getErrors([form])

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        
        context = {
            "form": form,
            'errors': errors,
        }
        return render(request, 'authentication/login.html', context)
    
class RegisterUser(View):
    def get(self, request):
        registerForm = CustomUserCreationForm()

        context = {
            'form' : registerForm
        }

        return render(request, 'authentication/registerUser.html', context)
    
    def post(self, request):
        registerForm = CustomUserCreationForm(request.POST)

        errors = getErrors([registerForm])

        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.save()

            return redirect('alert_user_inactive')
        
        context = {
            'errors' : errors,
            'form' : registerForm
        }

        return render(request, 'authentication/registerUser.html', context)