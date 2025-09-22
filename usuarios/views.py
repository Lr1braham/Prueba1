# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def home(request):
    return render(request, "usuarios/home.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # guarda automáticamente en PostgreSQL
            return redirect('success')  # redirige a una página de éxito
    else:
        form = ContactForm()
    return render(request, 'usuarios/contact.html', {'form': form})

def success_view(request):
    return render(request, 'usuarios/success.html')

def login_view(request):
    return render(request, "usuarios/login.html")  # si creas login.html

#aaaaaaaaa
def contact_list(request):
    contacts = Contact.objects.all()  # SELECT * FROM contact;
    return render(request, "Contact.html", {"form": form})# lista de contactos

def login_view(request):
    contacts = Contact.objects.all()  # Trae todos los registros
    return render(request, "Login.html", {"contacts": contacts})
