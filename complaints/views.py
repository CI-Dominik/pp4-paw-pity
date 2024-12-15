from django.shortcuts import render, redirect
from .forms import CommentComplaintForm
from reports.models import Comment
from .models import CommentComplaint


def complain_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        form = CommentComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.comment = comment
            complaint.user = request.user
            complaint.save()
            return redirect('animal_detail', animal_id=comment.animal.id)
    else:
        form = CommentComplaintForm()
    return render(request, 'complaints/complain_comment.html', {'form': form, 'comment': comment})


def view_complaints(request):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)
    complaints = CommentComplaint.objects.all()
    return render(request, 'complaints/complaints_list.html', {'complaints': complaints})


def remove_comment(request, comment_id):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('view_complaints')


def delete_complaint(request, complaint_id):
    if not request.user.is_superuser:
        return render(request, '403.html', status=403)
    complaint = CommentComplaint.objects.get(id=complaint_id)
    complaint.delete()
    return redirect('view_complaints')
