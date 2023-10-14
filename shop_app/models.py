from django.db import models

# Create your models here.
class Slider (models.Model):
    title= models.CharField(max_length=50)
    title1= models.CharField(max_length=50)
    description= models.TextField()
    button_tag= models.CharField(max_length=20)
    image= models.ImageField(upload_to='slider_image/')

    def __str__(self):
        return str(self.title)

class Catagory(models.Model):

    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)