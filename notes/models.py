from django.db import models
from accounts.models import MyUser
from django_cleanup.cleanup import cleanup_select

# Create your models here.
@cleanup_select
class Profile(models.Model):
    user=models.OneToOneField(to=MyUser, on_delete=models.SET_NULL, null=True)
    photo=models.ImageField(upload_to='profile', null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    user=models.ForeignKey(to=MyUser, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=200, default='test note')
    description=models.TextField(max_length=500, default='test description')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)