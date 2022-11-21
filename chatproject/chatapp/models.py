from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GroupName(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class GroupDetails(models.Model):
    group_name = models.ForeignKey(GroupName, on_delete=models.CASCADE, related_name='group_name', null=True)
    members = models.ForeignKey(User, on_delete=models.CASCADE, related_name='members', null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return str(self.group_name)
        return str(self.group_name)

    def Time(self):
        self.date = timezone.now()
        self.save()