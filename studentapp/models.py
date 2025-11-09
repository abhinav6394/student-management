from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    branch = models.CharField(max_length=50)
    marks = models.FloatField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name