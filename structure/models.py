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


    # def publish(self):
    #     self.change_date = timezone.now()
    #     self.save()

    # def save(self):
    #     print (self.owner, self.editors, self.title, self.description)
    #     print (self)

    def __str__(self):
        return self.title

# class Editors(models.Model):
#     table = models.ManyToManyField(Table)
#     editor = models.ManyToManyField(Table)


#     def __str__(self):
#         return self.title
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
