from django.urls import path
from . import views  # Certifique-se de que está importando views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('recuperar_senha/', views.recuperar_senha, name='recuperar_senha'),
    path('lojas/',views.lojas_view, name='lojas'),
    path('chats', views.chats_view, name='chats'),
    path('descubra/', views.descubra_view, name='descubra'),
    
]