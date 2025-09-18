from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.contraseña = make_password(self.cleaned_data["contraseña"])
        if commit:
            usuario.save()
        return usuario
