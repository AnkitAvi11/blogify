from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model) : 
    user = models.OneToOneField(User, models.CASCADE)
    profile_image = models.ImageField(upload_to='images/%Y/%m/', default='default.png')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(default=None, blank=True, null=True, max_length=200)

    #   social connections links
    website = models.URLField(default=None, blank=True, null=True)
    linkedin = models.URLField(default=None, blank=True, null=True)
    github = models.URLField(default=None, blank=True, null=True)

    #   work details
    work = models.CharField(default=None, blank=True, null=True, max_length=200)
    achievements = models.TextField(default=None, blank=True, null=True, max_length=200)
    skills = models.TextField(default=None, blank=True, null=True, max_length=200)

    def __str__(self) : 
        return self.user.username

    def save(self, *args, **kwargs) : 
        try : 
            current = UserProfile.objects.get(id=self.id) 
            if current.profile_image != self.profile_image and current.profile_image != 'default.png' : 
                current.profile_image.delete()

        except : 
            pass

        super().save(*args, **kwargs)


def createProfile(sender, **kwargs) : 
    if kwargs['created'] : 
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)