from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('saree', 'Saree'),
        ('dryfruit', 'Dry Fruit'),
        ('healthmix', 'Health Mix'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.category == 'saree' and not self.expiry_date:
            self.expiry_date = now().date() + timedelta(days=3)
        super().save(*args, **kwargs)