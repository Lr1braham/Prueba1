# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

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
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'usuarios/success.html')
