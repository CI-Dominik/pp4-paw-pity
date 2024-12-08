from django.shortcuts import render, redirect
from animals.models import Animal
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment
from django.contrib import messages


def reports_view(request):
    animals = Animal.objects.filter(is_found=False)
    paginator = Paginator(animals, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reports/reports.html', {'page_obj': page_obj})


def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    comments = Comment.objects.filter(animal=animal, is_approved=True)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.animal = animal
                comment.save()
                return redirect('animal_detail', animal_id=animal_id)
            else:
                if form.cleaned_data['content'] == '':
                    messages.error(request, 'Please enter a comment.')
                else:
                    messages.error(request, 'Please correct the errors in your submitted form.')
        else:
            messages.error(request, 'You must be logged in to comment.')
    else:
        form = CommentForm()
    return render(request, 'reports/animal_detail.html', {'animal': animal, 'comments': comments, 'form': form})