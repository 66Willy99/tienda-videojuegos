from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Juego

# Create your views here.
def lista_juegos(request):
    juegos = Juego.objects.all().order_by('id') # Mantenemos un orden consistente
    paginator = Paginator(juegos, 6) # Mostramos 6 juegos por pagina 
    
    # Obtenemos el numero de pagina desde la URL (?page=2)
    page_number = request.GET.get('page')
    
    # Obtenemos los objetos de esa pagina
    page_obj = paginator.get_page(page_number)
    
    # Pasamos la plantilla como 'lista_juegos'
    contexto_catalogo_juegos={'lista_juegos': page_obj}
    
    return render(request, 'catalogo/lista-juegos.html', contexto_catalogo_juegos)