from django.shortcuts import render
from catalogo.models import Juego

# Create your views here.
def lista_juegos(request):
    juegos = Juego.objects.all()
    contexto_catalogo_juegos={'lista_juegos': juegos}
    return render(request, 'catalogo/lista-juegos.html', contexto_catalogo_juegos)