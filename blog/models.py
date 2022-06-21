from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title =  models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_post = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

