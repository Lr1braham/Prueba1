# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages # para mensajes flash
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):
    return render(request, "usuarios/home.html")

def success_view(request):
    return render(request, 'usuarios/success.html')

def login_view(request):
    return render(request, "usuarios/login.html")

from django.shortcuts import render

# Vista para el dashboard (página protegida)

def dashboard_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    user = Contact.objects.get(id=user_id)
    return render(request, "usuarios/dashboard.html", {"user": user})

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
                return redirect("dashboard")  # 👈 redirige al login
    else:
        form = ContactForm()

    return render(request, "usuarios/contact.html", {"form": form})



