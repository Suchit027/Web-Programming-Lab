from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateField()
    salary = models.IntegerField(default= 0)
    designation = models.CharField(max_length = 100)
    def __str__(self):
        return self.name