from django.conf import settings
from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=50)
    target = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
