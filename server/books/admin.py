from django.contrib import admin
from .models import Book

class boodAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description']
