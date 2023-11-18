
from django.contrib import admin
from django.urls import include, path

from .views import all_tables

urlpatterns = [
    path('', all_tables, name='all_tables'),
]
