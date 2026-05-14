from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    yop = models.IntegerField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    coach = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Finance(models.Model):
    team = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team
    






