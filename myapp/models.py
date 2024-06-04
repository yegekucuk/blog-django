from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateField()
    image = models.ImageField(upload_to='static/img_uploaded/')
    paragraph = models.TextField(max_length=500)

class Review(models.Model):
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)