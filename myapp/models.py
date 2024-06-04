from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateField()
    image = models.ImageField(upload_to='static/img_uploaded/')
    paragraph = models.TextField(max_length=500)