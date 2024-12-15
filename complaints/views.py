from django.shortcuts import render, redirect
from .forms import CommentComplaintForm
from reports.models import Comment
from .models import CommentComplaint
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View

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


class ViewComplaintsView(PermissionRequiredMixin, View):
    permission_required = 'is_superuser'
    raise_exception = True

    def get(self, request):
        complaints = CommentComplaint.objects.all()
        return render(request, 'complaints/complaints_list.html', {'complaints': complaints})