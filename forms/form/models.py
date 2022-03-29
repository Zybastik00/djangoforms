from django.db import models

class Animals(models.Model):
    name=models.CharField(max_length=30)
    type1=models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)+' '+str(self.type1)

class Char(models.Model):
    name=models.ForeignKey(Animals, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)+str(self.color)+str(self.age)