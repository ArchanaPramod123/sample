from django.contrib import admin
from .models import Category
from .models import Product
from .models import Author
from .models import Book

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Book)