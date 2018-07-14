import jsonfield

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Main(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="owner")
    editors = models.ManyToManyField('auth.User', related_name='editors') 
    title = models.CharField(max_length=200)
    table_body = jsonfield.JSONField()
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
