from django.shortcuts import render
from .models import Warehouse, Product, Client, Sale


def all_tables(request):
    warehouses = Warehouse.objects.all()
    products = Product.objects.all()
    clients = Client.objects.all()
    sales = Sale.objects.all()

    return render(request, 'index.html', {
        'warehouses': warehouses,
        'products': products,
        'clients': clients,
        'sales': sales,
    })
