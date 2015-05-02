from django import forms
from comments.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = {'author', 'recipe', 'date'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }
