from django.db import models
from reports.models import Comment
from django.contrib import admin


class CommentComplaint(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    list_display = ('comment', 'reason', 'created_at')

    def __str__(self):
        return f"Complaint for comment {self.comment}: {self.reason}"


@admin.register(CommentComplaint)
class CommentComplaintAdmin(admin.ModelAdmin):
    list_display = ('comment', 'reason', 'created_at')
