from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PUser(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    dp = models.ImageField(upload_to='prof_pics', blank=True)

    def __str__(self):
        return self.user.username
