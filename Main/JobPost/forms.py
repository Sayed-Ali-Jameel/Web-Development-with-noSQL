from django import forms
from django.forms import (CharField, EmailField)
from .models import Post

class PostForm(forms.ModelForm):
    title = CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )
    description = CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        })
    )
    responsibility = CharField(required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'responsibility'
        })
    )
    qualifications = CharField(required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'qualifications'
        })
    )

    class Meta:
            model = Post
            fields = ['title', 'description', 'responsibility', 'qualifications']
            
