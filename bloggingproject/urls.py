
from django.contrib import admin
from django.urls import path, include

#   url patterns
urlpatterns = [
    #   admin route
    path('admin/', admin.site.urls),

    #   own applications below here
    path('account/', include('account.urls')),

    #   social auth urls below here
    path('oauth/', include('social_django.urls'), name='social')
]
