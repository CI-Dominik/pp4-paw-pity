from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(
        request,
        'main/index.html',
        {}
    )


def csrf_failure(request, reason=""):
    return redirect('home')
