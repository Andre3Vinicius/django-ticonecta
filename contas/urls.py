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
    path('home/ticomunica/', views.ticomunica_view, name='ticomunica'),
    path('ticomunica/desenvolvedores/', views.desenvolvedores_view, name='desenvolvedores'),
    path('ticomunica/designers/', views.designers_view, name='designers'),
    path('ticomunica/analista_dados/', views.analista_dados_view, name ='analista_dados'),
    path('ticomunica/qas/', views.qas_view, name='qas')
]