from django.db import models

# Create your models here.
class Weather(models.Model):
    img=models.ImageField( upload_to='static/img', height_field=None, width_field=None, max_length=None)
