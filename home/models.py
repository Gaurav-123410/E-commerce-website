from django.db import models

# makemigrations= create changes and store in a file 
# migrate= apply the pending hanges created by makemigrations


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    additionaldetails = models.TextField()
    date = models.DateField()

#MAIN CHAHTA HU KI JISNE FORM FILL KIYA H USI KA DATA NAME SE STORE HO USKE LIYE


    def __str__(self):
        return self.name
    