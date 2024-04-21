from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'photo', 'created_at', 'updated_at']

class NoteAdmin(admin.ModelAdmin):
    list_display=['user', 'title', 'created_at', 'updated_at']

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Note, NoteAdmin)