from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import CartItem

@login_required
def order_create(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        return redirect('cart_detail')

    if request.method == 'POST':
        # считаем итого
        total = sum(item.total_price() for item in cart_items)

        # создаём заказ
        order = Order.objects.create(
            user=request.user,
            total_price=total
        )

        # создаём позиции заказа
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # очищаем корзину
        cart_items.delete()

        return redirect('order_detail', pk=order.pk)

    total = sum(item.total_price() for item in cart_items)
    return render(request, 'orders/order_create.html', {
        'cart_items': cart_items,
        'total': total,
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})