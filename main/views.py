from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Главная',
        'content': "Магазин",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': "О нас",
        'text_on_page': "Текст"
    }

    return render(request, 'main/about.html', context)