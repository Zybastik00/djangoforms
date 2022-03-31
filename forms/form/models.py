from django.db import models

class People(models.Model):
    number_phone=models.CharField(max_length=13)
    name=models.CharField(max_length=12)
    password=models.CharField(max_length=13)
    def __str__(self):
        return str(self.name)+' '+str(self.number_phone)

