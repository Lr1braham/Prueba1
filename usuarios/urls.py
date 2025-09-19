from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from usuarios.views import home, registro   # 👈 Importamos desde la app usuarios

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("admin/", admin.site.urls),
    path("registro/", registro, name="registro"),  # /registro/ → vista de registro
    path("", home, name="home"),  # / → vista de bienvenida
]
