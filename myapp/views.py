from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import *

def index(request):
    top_sneaker_categories = TopSneakerCategory.objects.all()
    return render(request, 'base.html', {'top_sneaker_categories': top_sneaker_categories})

def product(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'product.html', {'sneakers': sneakers})

def shoe_detail(request, pk):
    models_dict = {
       'sneaker': Sneaker,
        'top_sneaker': TopSneaker,
       'shoes': Shoes,
    }

    shoe = None
    for model in models_dict.values():
        try:
            shoe = model.objects.get(pk=pk)
            break
        except model.DoesNotExist:
            continue

    if shoe is None:
        return render(request, '404.html', status=404)

    return render(request,'shoe_detail.html', {'shoe': shoe})
