from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required
from .models import Animal
from django.core.paginator import Paginator
from django.contrib import messages


# View to show user's animals
@login_required
def animals(request):
    message = request.session.get('message')
    animal_list = Animal.objects.filter(owner=request.user)
    paginator = Paginator(animal_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "animals/animals.html",
        {'animal_list': animal_list, 'page_obj': page_obj, 'message': message}
    )


# View to add an animal to profile
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


# View to edit an animal from profile
@login_required
def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    success_message = None
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            name = form.cleaned_data.get('name').lower()
            owner = request.user

            if Animal.objects.filter(name__iexact=name.lower(), owner=owner).exclude(id=animal.id).exists():
                form.add_error(
                    'name', f'You have already registered an animal with that name.'
                )
                return render(request, 'animals/edit_animal.html', {'form': form})

            else:
                form.save()
                success_message = f"{animal.name} successfully updated!"
                return render(
                    request,
                    'animals/edit_animal.html',
                    {
                        'form': form,
                        'success_message': success_message
                    }
                )

    else:
        form = AnimalForm(instance=animal)

    return render(
        request,
        'animals/edit_animal.html',
        {'form': form, 'success_message': success_message}
    )


# View to delete an animal from profile
@login_required
def delete_animal(request, animal_id):
    queryset = Animal.objects.all()
    animal = get_object_or_404(queryset, pk=animal_id)

    if animal.owner == request.user:
        animal.delete()
        message = 'Animal deleted!'
    else:
        message = 'You can only delete your own animals!'

    messages.warning(request, message)
    return redirect('animals')
