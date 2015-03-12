from django.contrib import admin

from .models import Gallery, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)
