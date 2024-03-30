from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def layout(request):
    return render(request, 'blank_layout.html')

def list_products(request):
    return render(request, 'products.html')

def detail_product(request):
    return render(request, 'product_details.html')

