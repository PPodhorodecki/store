from django.shortcuts import render, get_object_or_404

from sklep.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'sklep/products.html', {'products': products})

def product(request, pk):
    item = get_object_or_404(Product, pk=pk)

    return render(request, 'sklep/product.html' ,{'product': item})