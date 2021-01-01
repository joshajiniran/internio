from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    linkedin = models.CharField(max_length=128, null=True, blank=True)
    github = models.CharField(max_length=128, null=True, blank=True)
    cv = models.FileField(upload_to='documents/',
                          help_text='Advisable to use your name as filename',
                          null=True)
    avatar = models.FileField(upload_to='gallery/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField()

    def __str__(self):
        return self.username
