from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


def home(request):
    # 1--> return HttpResponse('HomePage')
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)

