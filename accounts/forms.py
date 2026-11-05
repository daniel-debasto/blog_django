from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia', 'avatar', 'link_web']
