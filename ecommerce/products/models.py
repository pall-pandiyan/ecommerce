from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
