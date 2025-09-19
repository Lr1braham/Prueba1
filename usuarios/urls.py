from django.urls import path
from . import views
from django.contrib import admin
from app.views import home, registro   # ajusta "app" al nombre real de tu app

urlpatterns = [
    path("registro/", views.registro, name="registro"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registro/", registro, name="registro"),
    path("", home, name="home"),   # <--- Página de bienvenida
]
