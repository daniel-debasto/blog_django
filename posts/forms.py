from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el título de la publicación'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribe el contenido aquí...'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
