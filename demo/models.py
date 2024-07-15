from django.db import models
from cloudinary.models import CloudinaryField

class PhotoUpload(models.Model):
    image = CloudinaryField('image')
