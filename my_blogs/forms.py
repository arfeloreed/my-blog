from django import forms

from .models import Comment


# forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {
            "comment": "Write a comment",
        }
