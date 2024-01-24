from django.db import models

class ToDo(models.Model):
    name=models.CharField(max_length=50)
    dis=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
    
