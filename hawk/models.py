from django.db import models

# Create your models here.
class heroImage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to = 'hero_image/')

    def __str__(self):
        return self.title
    
class Updates(models.Model):
    title = models.CharField(max_length=200)
    news_image = models.ImageField(upload_to = 'news_image/')

    def __str__(self):
        return self.title 

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='athlete_photos/',null=True)

    def __str__(self):
        return self.name