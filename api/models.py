from django.db import models

# Create your models here.

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('FOOD','Food'),
        ('BOOKS','Books'),
        ('ELECTRONICS', 'Electronics'),
        ('CLOTHING', 'Clothing')
    ]

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=False)
    price = models.FloatField()
    stock = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES,default='')
    
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


