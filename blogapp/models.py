from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Blog (models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=False, null=False)
    thumbnail = models.ImageField(upload_to = "blogs/%Y/%m/")

    pub_date = models.DateTimeField(default=timezone.now())

    likes = models.ManyToManyField(User, related_name='user_likes')
    
    def __str__(self) : 
        return self.title

    def save(self, *args, **kwargs) : 
        try : 
            this = Blog.objects.get(id=self.id)
            if this.thumbnail != self.thumbnail : 
                this.thumbnail.delete()

        except : 
            pass

        return super().save(*args, **kwargs)
