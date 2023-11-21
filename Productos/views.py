from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Productos(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)


def personalized_products(request):
    personalized_products = Product.objects.filter(is_personalized=True)
    context = {'personalized_products': personalized_products}
    return render(request, 'productos Personalizados.html', context)