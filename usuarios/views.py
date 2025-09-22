# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages # para mensajes flash

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
    return render(request, "usuarios/login.html")

from django.shortcuts import render

# Vista para manejar el login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Contact.objects.get(email=email, password=password)
            # Guardamos la sesión
            request.session["user_id"] = user.id
            request.session["user_name"] = user.name
            messages.success(request, f"Bienvenido {user.name}")
            return redirect("dashboard")  # redirige a otra página después de login
        except Contact.DoesNotExist:
            messages.error(request, "Correo o contraseña incorrectos")

    return render(request, "usuarios/login.html")

# Vista para el dashboard (página protegida)

def dashboard_view(request):
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")

    if not user_id:
        return redirect("login")  # si no hay sesión vuelve al login

    return render(request, "dashboard.html", {"user_name": user_name})

