from django.db import models

# Create your models here.
class AddUser(models.Model):
    First_name=models.CharField(max_length=40)
    Last_name=models.CharField(max_length=40)
    Ph_no=models.IntegerField()
    Email = models.EmailField(primary_key=True)
    Password = models.CharField(max_length=200)
    def __str__(self):
        return self.Email
