from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=120)
    prodcuctDescription = models.TextField(blank=True, null=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdatedAt = models.DateTimeField(auto_now=True)
    maxQuantityPerOrder = models.IntegerField(default=5, help_text="Maximum quantity allowed per order for this product.")

    def __str__(self):
        return self.productName