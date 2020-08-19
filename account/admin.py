from django.contrib import admin

# Register your models here.
from .models import UserProfile, Follower, Notifications

admin.site.register(UserProfile)
admin.site.register(Follower)
admin.site.register(Notifications)