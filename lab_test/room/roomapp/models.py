from django.db import models

# Create your models here.
class Room(models.Model):
    price = models.IntegerField(default= 0)
    bhk = models.IntegerField(default= 1, choices= [[1, '1'], [2, '2'], [3, '3']])
    name = models.CharField(max_length = 100)
    allocated = models.IntegerField(default= 0)
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    def __str__(self):
        return self.name