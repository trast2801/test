from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    title = "Главная страница"
    head = "Главная"
    context = {
        'title' : title,
        'head': head,
    }
    return render(request, 'platform.html', context)

def shop_dict(request):
    shop = " Магазин "
    menu_shop = ' Игры '

    context = {
        'title': shop,
        'head': menu_shop,
        'games': ["Atomic Heart", "Cyberpunk 2077"],

    }
    return render(request, 'games.html', context)

def games(request):
    return render(request, 'games.html')

def basket(request):
    return render(request, 'cart.html')