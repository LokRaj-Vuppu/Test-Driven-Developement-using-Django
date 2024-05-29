from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'Posts/{filename}'



class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_file = models.FileField(upload_to=generate_filename, null=True, max_length=300)

    def __str__(self) -> str:
        return f"{self.title} - {self.body}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.pk})
