from django import forms
from .models import Comment


# Form for adding a comment
class CommentForm(forms.ModelForm):

    # Form fields
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': 'Your comment:',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    # Custom validation
    def clean_content(self):
        content = self.cleaned_data.get('content', '')

        # Check if the comment is empty
        if not content:
            raise forms.ValidationError('Please enter a comment.')
        # Check if the comment is at least 20 characters long
        if len(content) < 20:
            raise forms.ValidationError('The comment must be at least 20 characters long.')
        # Check if the comment is at most 255 characters long
        if len(content) > 255:
            raise forms.ValidationError('The comment must be at most 255 characters long.')

        return content
