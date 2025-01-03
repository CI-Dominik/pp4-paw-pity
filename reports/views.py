from django.shortcuts import render, redirect
from animals.models import Animal
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# View to show all reports
def reports_view(request):
    animals = Animal.objects.all().order_by('-id')
    paginator = Paginator(animals, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reports/reports.html', {'page_obj': page_obj})


# View to show a specific report
def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    comments = Comment.objects.filter(animal=animal)

    # Handle form submission
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.animal = animal
                comment.save()
                messages.success(
                    request,
                    'Your comment was successfully added.'
                    )
                return redirect('animal_detail', animal_id=animal_id)
            else:
                messages.error(
                    request,
                    'Please correct the errors in your submitted form.'
                    )
        else:
            messages.error(request, 'You must be logged in to comment.')
    else:
        form = CommentForm()

    return render(request, 'reports/animal_detail.html', {
        'animal': animal,
        'comments': comments,
        'form': form
    })


# View to edit a comment
@login_required
def edit_comment(request, animal_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    # Check if the user is the author of the comment
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('animal_detail', animal_id=animal_id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'reports/edit_comment.html', {
            'form': form,
            'comment': comment
            })
    else:
        return render(request, '403.html', status=403)


# View to delete a comment
@login_required
def delete_comment(request, animal_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    # Check if the user is the author of the comment
    if request.user == comment.user:
        comment.delete()
        return redirect('animal_detail', animal_id=animal_id)
    else:
        return render(request, '403.html', status=403)
