# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages # para mensajes flash
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Vista para la página de inicio
def home(request):
    return render(request, "usuarios/home.html")

def success_view(request):
    return render(request, 'usuarios/success.html')

def login_view(request):
    return render(request, "usuarios/login.html")
'''
@login_required
def dashboard_view(request):
    return render(request, "usuarios/dashboard.html", {"user": request.user})
'''
@login_required
def dashboard_view(request):
    usuarios = User.objects.all()  # trae todos los usuarios
    return render(request, "usuarios/dashboard.html", {"usuarios": usuarios})

def logout_view(request):
    request.session.flush()
    return redirect("login")

# Vista para manejar el login

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Django usa "username" aunque sea email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {user.email}")
                return redirect("dashboard")  # cambia "home" a la url que quieras
            else:
                messages.error(request, "Email o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, "usuarios/login.html", {"form": form})

# Vista para manejar el registro

def register_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Ese usuario ya existe.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
                return redirect("success")  # 👈 redirige al login
    else:
        form = ContactForm()

    return render(request, "usuarios/contact.html", {"form": form})

# Vista para el dashboard con mensajes privados

from .forms import MensajeForm
from .models import Mensaje

@login_required
def dashboard_view(request):
    # Formulario de nuevo mensaje
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect("dashboard")
    else:
        form = MensajeForm()

    # Mensajes recibidos por el usuario logueado
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user).order_by("-fecha_envio")

    return render(request, "usuarios/dashboard.html", {
        "form": form,
        "mensajes": mensajes_recibidos,
    })







