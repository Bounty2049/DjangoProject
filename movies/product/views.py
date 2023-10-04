from django.shortcuts import render
from product.models import Movie

def index(request):
    context = {
        'title': 'Стартапы с обучающими видео',
        'movie': Movie.objects.all()
        }
    return render(request, 'product/index.html', context=context)
