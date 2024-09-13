from django.contrib import admin
from .models import Pen
from .models import Store

# Register your models here.
admin.site.register(Pen)
admin.site.register(Store)