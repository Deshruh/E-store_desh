from django.db import models
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to="product_images")
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    tags = models.ForeignKey(
        to=ProductTag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Product: {self.username} | Category: {self.category}"


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart by {self.user.username} | Product: {self.product.name}"


class Wishlist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist by {self.user.username} | Product: {self.product.name}"
