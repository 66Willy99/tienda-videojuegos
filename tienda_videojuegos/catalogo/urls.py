from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name='catalogo'),
    path('<int:pk>/', views.detalle_juego, name='detalle-juego')
]
