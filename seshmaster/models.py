from django.db import models

class User(models.Model):

    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Image(models.Model):

    
    user = models.ForeignKey(User) 
    
    def __str__(self):
        return self.score

class Nightclub(models.Model):

    image = models.ForeignKey(Image)
    music_genre = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=400)
    average_score=models.CharField(max_length=10)

    def __str__(self):
        return self.score

class Review(models.Model):

    nightclub = models.ForeignKey(Nightclub)
    user = models.ForeignKey(User) 
    score = models.CharField(max_length=10)
    Comment = models.CharField(max_length=350)

    def __str__(self):
        return self.score




