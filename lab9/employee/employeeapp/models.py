from django.db import models

# Create your models here.
class Works(models.Model):
    name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    salary = models.IntegerField(default= 0)
    def __str__(self):
        return self.name

class Lives(models.Model):
    name = models.ForeignKey(Works, on_delete= models.CASCADE)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    def __str__(self):
        return self.city