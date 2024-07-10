from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="my")
    date = models.DateField(auto_now_add=True)