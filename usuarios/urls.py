from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Página de inicio
    path('contact/', views.contact_view, name='contact'),  # Formulario
    path('success/', views.success_view, name='success'),  # Éxito
    path("login/", views.login_view, name="login"), # página de login
    path("contacts/", views.contact_list, name="contact_list"),# lista de contactos
]

