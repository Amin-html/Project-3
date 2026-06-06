# from django.db import models
# from products.models import Product
#
# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Ожидает'),
#         ('processing', 'В обработке'),
#         ('completed', 'Выполнен'),
#         ('cancelled', 'Отменён'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='pending')
#     total_price = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f"Заказ #{self.pk} - {self.user}"
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.IntegerField() # цена на момент заказа
#
#     def __str__(self):
#         return f"{self.product} x{self.quantity}"
#
# # Create your models here.
