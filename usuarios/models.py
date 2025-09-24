from django.db import models

class Contact(models.Model):
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, default="user_default")  # campo de nombre de usuario
    #message = models.TextField()
    #phone = models.CharField(max_length=20, blank=True, null=True)   # ✅ nuevo campo
    #subject = models.CharField(max_length=200, blank=True, null=True) # ✅ nuevo campo
    password = models.CharField(max_length=128, default="123456")# campo de contraseña
    
    def __str__(self):
        return f"{self.name} - {self.email}"

# Modelo para mensajes privados entre usuarios

from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="mensajes_enviados", on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name="mensajes_recibidos", on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.remitente.username} para {self.destinatario.username}"
