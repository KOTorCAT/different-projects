from django.db import models

# Create your models here.

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"