from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Player(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.username