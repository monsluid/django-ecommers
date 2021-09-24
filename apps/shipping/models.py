from django.db import models
from apps.product.models import Product

# ------------------------------------------------------------------------------------>
# Model Shipping

class Shipping(models.Model):
    quantity = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default = True)