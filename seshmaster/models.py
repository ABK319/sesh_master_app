from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile', blank=True)


    def __str__(self):
        return self.user.username



class Nightclub(models.Model):

    name = models.CharField(max_length=128,help_text="Please enter the location name.")
    music_genre = models.CharField(max_length=100,help_text="What is the music like here?")
    price = models.CharField(max_length=128,help_text="Price range?")
    description = models.CharField(max_length=400,help_text="Little inside on what the place is like ;)")
    location = models.CharField(max_length=128,help_text="Where can people find this?")
    average_score=models.IntegerField()
    img = models.ImageField(upload_to='images', blank=True)
    
   

    def __str__(self):
        return self.name

class Image(models.Model):

    
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='images', blank=True)
    location = models.ForeignKey(Nightclub)
    
    



class Review(models.Model):

    nightclub = models.ForeignKey(Nightclub)
    user = models.ForeignKey(User) 
    score = models.IntegerField()
    Comment = models.CharField(max_length=350)

    def __str__(self):
        return self.score




