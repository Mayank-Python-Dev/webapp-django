from django.core.files import images
from django.db import models
# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to = 'Pictures')
    description = models.TextField()
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)
