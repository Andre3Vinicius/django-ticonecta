
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('contas.urls')),
    path('', RedirectView.as_view(url='/contas/login/')),  # Redireciona a raiz para a página de login
    path('recuperar_senha/', auth_views.PasswordResetView.as_view(), name='recuperar_senha'),
    path('recuperar_senha/confirmar/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('senha_alterada/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]