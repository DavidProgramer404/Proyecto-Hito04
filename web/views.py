from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# import autenticacion
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

# Metodo

def index(request):
    products = Product.objects.filter(sale=False)
    context = {'products': products,}
    return render(request, 'product/index.html',context)

# create
def create(request):
    return render(request, 'product/create.html')

def bienvenido(request):
    return render(request, 'product/bienvenido.html')

# sale
@login_required
def sale(request):
    products = Product.objects.filter(sale=True)
    context = {'products': products,}
    return render(request, 'product/sale.html',context)


def productos_ofertas(request):
    products = Product.objects.all()  # Query para obtener todos los productos
    context = {
        'products': products
    }
    return render(request, 'productos_ofertas.html', context)


def custom_logout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión.')
    return redirect('registration/logout')


def bienvenido(request):
    products = Product.objects.all()  # Query para obtener todos los productos
    context = {
        'products': products
    }
    return render(request, 'product/bienvenido.html', context)