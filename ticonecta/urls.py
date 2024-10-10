"""
URL configuration for ticonecta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('contas.urls')),  # Certifique-se de que isso esteja correto
    path('recuperar_senha/', auth_views.PasswordResetView.as_view(), name='recuperar_senha'),
    path('recuperar_senha/confirmar/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('senha_alterada/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]