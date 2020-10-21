from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_hospede/', views.add_hospede, name='add_hospede'),
    path('list_hospedes', views.list_hospedes, name='list_hospedes'),
    path('add_compositor/', views.add_compositor, name='add_compositor'),
    path('list_compositores', views.list_compositor, name='list_compositores'),
    path('add_musica/', views.add_musica, name='add_musica'),
    path('list_musicas/', views.list_musica, name='list_musicas'),
    path('add_estrela/', views.add_estrela, name='add_estrela'),
    path('list_estrelas/', views.list_estrela, name='list_estrelas'),
    path('add_constelacao/', views.add_constelacao, name='add_constelacao'),
    path('list_constelacoes/', views.list_constelacao, name='list_constelacoes')]
