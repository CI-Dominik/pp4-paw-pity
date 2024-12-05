from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomUserRegistrationForm
from .forms import CustomLoginForm
from django.contrib.auth import logout


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        if request.method == 'POST':
            form = CustomLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    login_message = 'You have successfully logged in.'
                    return render(
                        request,
                        'main/index.html',
                        {
                            'login_message': login_message
                        }
                    )
        else:
            form = CustomLoginForm()
        return render(request, 'accountsystem/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        if request.method == 'POST':
            form = CustomUserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                register_message = 'You have successfully registered.'
                return render(
                        request,
                        'main/index.html',
                        {
                            'register_message': register_message
                        }
                    )
        else:
            form = CustomUserRegistrationForm()
        return render(request, 'accountsystem/register.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        logout(request)
        logout_message = 'You have successfully logged out.'
        return render(
            request,
            'main/index.html',
            {
                'logout_message': logout_message
            }
        )
