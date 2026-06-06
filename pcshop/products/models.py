from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)  # Ноутбуки, Мониторы, Комплектующие
    slug = models.SlugField(unique=True) # laptops, monitors, components

    def __str__ (self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField(default=0)  # количество на складе
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
