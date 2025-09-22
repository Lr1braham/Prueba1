from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)   # ✅ nuevo campo
    subject = models.CharField(max_length=200, blank=True, null=True) # ✅ nuevo campo

    def __str__(self):
        return f"{self.name} - {self.email}"
