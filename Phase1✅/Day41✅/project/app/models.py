from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="Post")
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)