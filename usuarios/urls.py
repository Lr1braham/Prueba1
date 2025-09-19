from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # / → página de bienvenida
    path("registro/", views.registro, name="registro"),  # /registro/ → página de registro
]


