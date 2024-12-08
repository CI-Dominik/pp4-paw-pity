from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    content = forms.CharField(label='Add your comment:', widget=forms.Textarea(attrs={'class': 'form-control my-3', 'rows': 3}))