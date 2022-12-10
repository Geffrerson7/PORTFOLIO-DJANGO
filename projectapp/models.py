from django.db import models

from django.db import models
from django.db.models.fields import CharField, URLField
from django.contrib.auth.models import User


class Project(models.Model):
    title = CharField(max_length=200)
    description = models.TextField()
    url_image = URLField(blank=True)
    url_github = URLField(blank=True)
    tags = CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
