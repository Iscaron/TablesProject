from django.db import models
from django.utils import timezone


class Table(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="owner")
    editors = models.ManyToManyField('auth.User', related_name='editors') #TODO: ????????????????????????
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    change_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.change_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

# class Editors(models.Model):
#     table = models.ManyToManyField(Table)
#     editor = models.ManyToManyField(Table)


#     def __str__(self):
#         return self.title

