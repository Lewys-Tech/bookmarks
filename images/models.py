from django.conf import settings
from django.db import models

# Create your models here.
class Image(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, blank=True)
    url=models.URLField(max_length=2000)
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
    description=models.TextChoices(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    
class Meta:
    indexes[models.indexes()]