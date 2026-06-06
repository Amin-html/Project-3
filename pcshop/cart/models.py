# from django.db import models
# from products.models import Product
#
# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1) # количество товара
#
#     def total_price(self):
#         return self.product.price * self.quantity
#
#     def __str__(self):
#         return f"{self.user} - {self.product} x{self.quantity}"
#
# # Create your models here.
