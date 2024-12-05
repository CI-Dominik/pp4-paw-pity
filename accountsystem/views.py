from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserRegistrationForm
from .forms import CustomLoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'accountsystem/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'You have successfully registered.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'accountsystem/register.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('home')

    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')