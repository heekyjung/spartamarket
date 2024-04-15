from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models


class Product(models.Model):
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    deleted = models.BooleanField(default=False)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="ProductLike", related_name="like_products"
    )


class ProductLike(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
