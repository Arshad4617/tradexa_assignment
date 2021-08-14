from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
