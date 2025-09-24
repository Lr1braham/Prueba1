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
