from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    number= models.CharField(max_length=12)
    email= models.CharField(max_length=50)
    desc= models.TextField()
    date= models.DateField()


    def __str__(self):
        return self.name
    