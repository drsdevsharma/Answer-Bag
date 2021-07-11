from django.db import models
from user.models import AddUser

# Create your models here.

class Create_query(models.Model):
    Email=models.ForeignKey(to=AddUser,on_delete=models.CASCADE)
    user=models.CharField(max_length=20)
    Qid=models.IntegerField()
    Title=models.CharField(max_length=40)
    Date=models.DateField()
    Query=models.CharField(max_length=2000)

    def __str__(self): # return Object name when object is retrieved 
        return f"{self.Email}"

class Answer_query(models.Model):
    Email=models.ForeignKey(to=AddUser,on_delete=models.CASCADE)
    Qid=models.IntegerField()
    Date=models.DateField()
    Answer=models.CharField(max_length=2000)
    def __str__(self):  # return Object name when object is retrieved 
        return f"{self.Email}"