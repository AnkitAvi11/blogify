from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model) : 
    user = models.OneToOneField(User, models.CASCADE)
    profile_image = models.ImageField(upload_to='images/%Y/%m/', default='default.png')
    bio = models.TextField(blank=True, null=True)

    def __str__(self) : 
        return self.user.username


def createProfile(sender, **kwargs) : 
    if kwargs['created'] : 
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)