""" Post forms."""

# Django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """ Post model form."""
    class Meta:
        # La configuracion de la clase en genral
        model = Post
        fields = {'user', 'profile', 'title', 'photo'}