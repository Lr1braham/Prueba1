from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validaciones básicas
        if not username or not email or not password1 or not password2:
            messages.error(request, "Todos los campos son obligatorios")
        elif password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado")
        else:
            # Crear usuario
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, "✅ Cuenta creada con éxito")
            return redirect("registro")  # Puedes redirigir al login en vez de registro

    return render(request, "usuarios/registro.html")

from django.shortcuts import render

def registro(request):
    return render(request, "../usuarios/registro.html")

def home(request):
    return render(request, "../usuarios/home.html")   # 👈 importante el prefijo usuarios/
