from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile', blank=True)


    def __str__(self):
        return self.user.username

class Image(models.Model):

    
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='images', blank=True)
    
    def __str__(self):
        return self.score

class Nightclub(models.Model):

    name = models.CharField(max_length=128,help_text="Please enter the location name.")
    music_genre = models.CharField(max_length=100,help_text="What is the music like here?")
    price = models.CharField(max_length=128,help_text="Price range?")
    description = models.CharField(max_length=400,help_text="Little inside on what the place is like ;)")
    location = models.CharField(max_length=128,help_text="Where can people find this?")
    average_score=models.CharField(max_length=10)
    image = models.ImageField(upload_to='images', blank=True)
   

    def __str__(self):
        return self.name

class Review(models.Model):

    nightclub = models.ForeignKey(Nightclub)
    user = models.ForeignKey(User) 
    score = models.CharField(max_length=10, help_text='What would you rate this nightclub?')
    Comment = models.CharField(max_length=350, help_text='What would you say about this nightclub (350 characters)')

    def __str__(self):
        return self.score

class NCImage(models.Model):

    
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='images', blank=True)
	


