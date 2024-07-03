from django import forms
from .models import Post
from django.utils.safestring import mark_safe

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'products', 'img']