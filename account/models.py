from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime

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

#   user profile creation automated
def createProfile(sender, **kwargs) : 
    if kwargs['created'] : 
        userprofile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)

#   Model for creating relation between users if they follow
class Follower(models.Model) : 

    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_set')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_set')
    relation_date = models.DateTimeField(default=datetime.now())

    def __str__(self) : 
        return "{} follows {}".format(self.user_from, self.user_to)

    def isFollowing(self, u_from, to) : 
        if Follower.objects.filter(user_from=u_from, user_to = to).exists() : 
            return True
        else : 
            return False


#   model for user notifications
class Notifications(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(default=None, blank=True, null=True)
    time_created = models.DateTimeField(default=datetime.now())
    is_read = models.BooleanField(default=False)

    def __str__(self) : 
        return self.title


