from django.db import models
from reports.models import Comment


class CommentComplaint(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint for comment {self.comment}: {self.reason}"
