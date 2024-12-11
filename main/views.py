from django.shortcuts import render
from django.shortcuts import redirect
from animals.models import Animal


def home(request):
    latest_animals = Animal.objects.all().order_by('-id')[:3]
    return render(
        request,
        'main/index.html',
        {'latest_animals': latest_animals}
    )


def csrf_failure(request, reason=""):
    return redirect('home')
