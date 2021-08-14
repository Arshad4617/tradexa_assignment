from django.db import models

# Create your models here.


class Post(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
