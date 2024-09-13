from django.db import models

# Create your models here.

    
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)

    def __str__(self) :
        return self.category_name
    


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    des = models.TextField(null=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    product_mark = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title