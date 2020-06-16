from django.db import models

class Content(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    img=models.ImageField(upload_to="sharma/images")
    url = models.URLField(blank=True)
class Pp(models.Model):
    ii=models.ImageField(upload_to='sharma/images')