from django.db import models

# Create your models here.
class Author(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.URLField()
    def __str__(self):
        return self.firstname

class Publisher(models.Model):
    name = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    website = models.URLField()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField(max_length = 100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete= models.CASCADE)
    def __str__(self):
        return self.title
    