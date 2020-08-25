from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin (admin.ModelAdmin) : 
    list_display = ('id', 'title', 'description', 'pub_date', 'user')
    list_display_links = ('id', 'title')

admin.site.register(Blog, BlogAdmin)