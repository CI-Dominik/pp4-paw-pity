from django.shortcuts import render, redirect
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required
from .models import Animal


@login_required
def animals(request):
    animal_list = Animal.objects.filter(owner=request.user)
    return render(
        request,
        "animals/animals.html",
        {'animal_list': animal_list}
    )


@login_required
def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            owner = request.user

            if Animal.objects.filter(name=name, owner=owner).exists():
                form.add_error(
                    'name', f'You have already registered {name}.'
                    )

            else:
                animal = form.save(commit=False)
                animal.owner = owner
                animal.save()
                return redirect('animals')
    else:
        form = AnimalForm()

    return render(request, 'animals/add_animal.html', {'form': form})
