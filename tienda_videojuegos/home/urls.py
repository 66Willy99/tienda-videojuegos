from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #ruta principal: llama  ala vista index
    path('contacto/', views.contacto, name='contacto') #ruta contacto; llama a la vista contacto
]
