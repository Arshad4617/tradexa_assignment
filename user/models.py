from django.db import models

# Create your models here.


class Post(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
