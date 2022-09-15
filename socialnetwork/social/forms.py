from django import forms
from .models import Post, Comment


class PostForms(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something!', }),
        max_length=400)

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': '3',
                                     'placeholder': 'Say something!', }),
        max_length=400)

    class Meta:
        model = Comment
        fields = ['comment']
