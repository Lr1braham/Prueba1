# en myapp/forms.py
# myapp/forms.py
from django import forms
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username','email', 'password']
        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control shadow-sm rounded-lg',
                'placeholder': 'Usuario',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control shadow-sm rounded-lg',
                'placeholder': 'Correo electrónico',
                'required': True,
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control shadow-sm rounded-lg',
                'placeholder': 'Contraseña',
                'required': True,
            }),
        }
        labels = {
            'email': 'Correo electrónico',
            'password': 'Contraseña',
            'username': 'Nombre de usuario',
        }

# Formulario de login

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")  # o email si configuras auth
    password = forms.CharField(widget=forms.PasswordInput)

# Formulario para mensajes privados

from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all(), label="Enviar a")

    class Meta:
        model = Mensaje
        fields = ["destinatario", "contenido"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 3, "placeholder": "Escribe tu mensaje aquí..."}),
        }
