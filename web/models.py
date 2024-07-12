from django.db import models

# Create your models here.


# crear class modelo product

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField()
    sale = models.BooleanField()

    def __str__(self):
        return self.name