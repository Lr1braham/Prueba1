# en myapp/forms.py
# myapp/forms.py
from django import forms
from .models import Contact


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
##aaaaaaaaaaaaa
