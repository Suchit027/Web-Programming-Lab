from django.db import models

# Create your models here.
class StudentCR(models.Model):
    name = models.CharField(max_length = 100)
    section = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Choice(models.Model):
    cr = models.ForeignKey(StudentCR, on_delete = models.CASCADE)
    vote = models.IntegerField(default= 0)
    def __str__(self):
        return self.vote