from django.db import models

class User(models.Model):

    name = models.CharField(max_length=128, unique=True,help_text= "How should we call you?")
    email = models.CharField(max_length=128, unique=True,help_text="How can we contact you?")
    password = models.CharField(max_length=128,help_text= "enter password")
    picture = models.ImageField(upload_to='profile', blank=True)


    def __str__(self):
        return self.name

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
    score = models.CharField(max_length=10)
    Comment = models.CharField(max_length=350)

    def __str__(self):
        return self.score




