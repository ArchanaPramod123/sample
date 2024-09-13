from django.db import models

# Create your models here.
class Pen(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand
    

class Store(models.Model):
    name = models.CharField(max_length=100)
    pens = models.ManyToManyField('Pen', related_name='stores')
    price = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

