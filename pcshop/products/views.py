from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    # 1. Сначала берём базовый QuerySet всех товаров
    products = Product.objects.all()
    categories = Category.objects.all()

    # 2. Получаем параметры из URL
    category_slug = request.GET.get('category', '')
    query = request.GET.get('q', '')

    # 3. Фильтруем по поисковому запросу (если он есть)
    if query:
        products = products.filter(name__icontains=query)

    # 4. Фильтруем по категории (если она выбрана)
    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    # 5. Передаём правильные ключи в контекст
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,  # Было 'category': categories (ошибка!)
        'current_category': current_category,
        'query': query,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
