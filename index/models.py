from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    subscriber = models.BooleanField(default=False)

class Coliseum(models.Model):
    model_id = models.CharField(max_length=100, default='coliseum')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=False)


class Fortress(models.Model):
    model_id = models.CharField(max_length=100, default='fortress')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=False)


class Pyramid(models.Model):
    model_id = models.CharField(max_length=100, default='pyramid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    public = models.BooleanField(default=False)


