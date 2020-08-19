
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#   url patterns
urlpatterns = [
    #   admin route
    path('admin/', admin.site.urls),

    #   own applications below here
    path('account/', include('account.urls')),

    #   social auth urls below here
    path('oauth/', include('social_django.urls'), name='social')
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
