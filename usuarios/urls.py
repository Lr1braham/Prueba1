from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Página de inicio
    path('contact/', views.contact_view, name='contact'),  # Formulario
    path('success/', views.success_view, name='success'),  # Éxito
    path("login/", views.login_view, name="login"), # página de login
    path("dashboard/", views.dashboard_view, name="dashboard"),# página protegida
    path("logout/", views.logout_view, name="logout"), # página de logout
]

