from django.db import models
from django.utils import timezone
# Create your models here.
class Article (models.Model):
    title= models.CharField(max_length=225)
    body = models.TextField()
    view = models.IntegerField(default=0)
    published_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title