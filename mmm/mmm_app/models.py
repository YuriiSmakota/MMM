import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    login = models.CharField(max_length=16, unique=True, null=False)
    password = models.CharField(max_length=16)
    email = models.EmailField()
    status = models.CharField()
