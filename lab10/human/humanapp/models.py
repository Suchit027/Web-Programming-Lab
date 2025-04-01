from django.db import models

# Create your models here.
class Human(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    def __str__(self):
        return self.first_name