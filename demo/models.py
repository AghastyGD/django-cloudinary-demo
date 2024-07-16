from django.db import models
from cloudinary.models import CloudinaryField

class PhotoUpload(models.Model):
    image = CloudinaryField('image')

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = CloudinaryField("image")
