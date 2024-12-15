from django import forms
from .models import CommentComplaint
from django.core.exceptions import ValidationError


class CommentComplaintForm(forms.ModelForm):
    class Meta:
        model = CommentComplaint
        fields = ['reason']

    def clean_reason(self):
        reason = self.cleaned_data['reason']
        if not reason:
            raise ValidationError('Please enter a reason for the complaint.')
        if len(reason) < 10:
            raise ValidationError('The reason must be at least 10 characters long.')
        return reason
