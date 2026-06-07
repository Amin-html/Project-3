from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    category_slug = request.GET.get('category', '')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
        category = None

    return render(request, 'products/product_list.html', {
        'products': products,
        'category' : categories,
        'current_category' : category,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product' : product})

# Create your views here.
