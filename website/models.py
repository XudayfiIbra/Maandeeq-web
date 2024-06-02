from django.db import models



class Product(models.Model):

    CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]      
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.IntegerField(choices=CHOICES, default=0)
    is_liked = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to='website/images')
