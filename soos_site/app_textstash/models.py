from django.db import models
import secrets

class Stash(models.Model):
    string_id = models.CharField(max_length=16, unique=True, editable=False, blank=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.string_id = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title