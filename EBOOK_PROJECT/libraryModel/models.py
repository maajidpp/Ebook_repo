from email.policy import default
from secrets import choice
from django.db import models

# Create your models here.
choices = (('Fantasy','Fantasy'),('Literary','Literary'),('Mystery','Mystery'),('Science Fiction','Science Fiction'),('Thriller','Thriller'))

class Ebooks(models.Model):
    Title = models.TextField()
    Author = models.TextField()
    Genre = models.CharField(max_length = 15,choices= choices )
    Review = models.IntegerField()
    Favorite = models.BooleanField(default = False)
    
    def __str__(self) :
        return self.Title