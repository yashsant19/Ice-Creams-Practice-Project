from django.db import models

# Create your models here.

# added by me to create a model to store data in database 
class Contact(models.Model):
    full_name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone =models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    
    # to show the name of the person in admin panel
    def __str__(self):
        return self.full_name