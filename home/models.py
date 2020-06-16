from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    commit_2 = models.CharField(null=True, blank=True, max_length=256,)
    commit_3 = models.BigIntegerField(null=True, blank=True,)
    commit_4 = models.BigIntegerField(null=True, blank=True,)
    commit_5 = models.DateTimeField(null=True, blank=True, auto_now=True,)
    commit_6 = models.CharField(null=True, blank=True, max_length=256,)
    commit8 = models.DecimalField(
        null=True, blank=True, max_digits=30, decimal_places=10,
    )
    test_1 = models.BooleanField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
