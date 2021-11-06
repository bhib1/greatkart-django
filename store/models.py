from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        # آرگ حالا دوتا آرگومان دارد یکی category slug و یکی هم product slug
        # سلف ینی همین کلاس پروداکت بالا، کتگوری هم همین کتگوری بالا که به کلاس پروداکت دادیم و .slug ینی سلاگ کتگوری
        # دومی هم ینی سلاگ پروداکت
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
