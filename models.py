from django.db import models
# Create your models here.
from datetime import datetime
# Create your models here.


class Useradd(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username




        

    
class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    message=models.TextField()
    
    created_at=models.DateTimeField(default=datetime.now)
    is_resolved=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    