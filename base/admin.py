from django.contrib import admin
from .models import PhotoType, Photo

admin.site.register([Photo, PhotoType])