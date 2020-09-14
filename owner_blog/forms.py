from django import forms
from .models import OwnerBlog


class BlogForm(forms.ModelForm):
    class Meta:
        model = OwnerBlog

        fields = ('title', 'thought_content', )
