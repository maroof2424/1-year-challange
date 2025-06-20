from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title