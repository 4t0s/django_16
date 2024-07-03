from django.db import models

class Post(models.Model):   
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    products = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
