# en myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages # para mensajes flash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

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
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            raw = form.cleaned_data.get("password", "").strip()
            contact.password = make_password(raw)   # <-- hash aquí
            contact.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("login")
    else:
        form = ContactForm()
    return render(request, "Contact.html", {"form": form})


# Vista para el dashboard (página protegida)

def dashboard_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")
    user = Contact.objects.get(id=user_id)
    return render(request, "Dashboard.html", {"user": user})

def logout_view(request):
    request.session.flush()
    return redirect("login")


# Vista para manejar el login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email","").strip()
        password = request.POST.get("password","").strip()
        user = Contact.objects.filter(email__iexact=email, password=password).first()
        if user:
            request.session["user_id"] = user.id
            return redirect("dashboard")
        else:
            messages.error(request, "Correo o contraseña incorrectos")
    return render(request, "Login.html")

