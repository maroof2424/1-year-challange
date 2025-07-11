from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='image',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title