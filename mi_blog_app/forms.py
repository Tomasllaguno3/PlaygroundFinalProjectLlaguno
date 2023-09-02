from django import forms
from .models import Author, Post, Comment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content']
