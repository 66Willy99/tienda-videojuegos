from django.shortcuts import render

# Create your views here.
def lista_juegos(request):
    juegos = [
        {'nombre': 'Dogo Racing', 'precio': 29.99, 'plataforma': 'PC, PS5, Xbox Series X'},
        {'nombre': 'Cyber Legends', 'precio': 49.99, 'plataforma': 'PC, PS5'},
        {'nombre': 'Fantasy Quest', 'precio': 39.99, 'plataforma': 'PC, Nintendo Switch'},
        {'nombre': 'Space Warriors', 'precio': 59.99, 'plataforma': 'PC, Xbox Series X'},
        {'nombre': 'Mystic Kingdom', 'precio': 34.99, 'plataforma': 'PS5, Nintendo Switch'},
        {'nombre': 'Battle Arena X', 'precio': 44.99, 'plataforma': 'PC, PS5, Xbox Series X'},
        {'nombre': 'Ocean Explorer', 'precio': 24.99, 'plataforma': 'PC'},
        {'nombre': 'Zombie Survival', 'precio': 19.99, 'plataforma': 'PC, PS4, Xbox One'},
        {'nombre': 'Speed Rivals', 'precio': 54.99, 'plataforma': 'PS5, Xbox Series X'},
        {'nombre': 'Dragon Chronicles', 'precio': 69.99, 'plataforma': 'PC, PS5, Xbox Series X, Nintendo Switch'}
    ]
    
    contexto_catalogo_juegos={'lista_juegos': juegos}
    return render(request, 'catalogo/lista-juegos.html', contexto_catalogo_juegos)