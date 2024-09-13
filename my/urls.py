# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_store_and_pen, name='index'),
]
