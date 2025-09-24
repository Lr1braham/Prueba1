from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.home, name='home'),           # Página de inicio
    path("contact/", views.register_view, name="contact"),  # ✅ ahora usa register_view
    path('success/', views.success_view, name='success'),  # Éxito
    path("dashboard/", views.dashboard_view, name="dashboard"),# página protegida
    path("logout/", views.logout_view, name="logout"), # página de logout
    path('login/', login_view, name='login'),# login
]

