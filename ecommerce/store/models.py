from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sub Categories"

    def __str__(self) -> str:
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=3)
    short_name = models.CharField(max_length=3, unique=True)
    conversion_rate_to_inr = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.slug

    class Meta:
        ordering = ["-modified_at"]
        verbose_name_plural = "Products"


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Tags"

    def __str__(self) -> str:
        return self.name


class TaggedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Tagged Products"

    def __str__(self) -> str:
        return self.product.name + " - " + self.tag.name
