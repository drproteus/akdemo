from django.contrib import admin
from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=1024)
    archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


admin.site.register(Resource)
