from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, null=True)
    link        = models.URLField(max_length=100, null=True)
    avatar      = models.ImageField(upload_to='avatares/', null=True, blank=True)