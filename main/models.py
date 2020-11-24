from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1024)
    subtitle = models.CharField(max_length=1024, blank=True)
    body = models.TextField()
    slug = models.CharField(max_length=1024, blank=True)
    archived = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = self.title.lower().replace(" ", "_")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

admin.site.register(Article)
