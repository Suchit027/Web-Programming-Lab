from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    visits = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    def __str__(self,):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    url = models.URLField()
    views = models.IntegerField(default = 0)
    def __str__(self, ):
        return self.title