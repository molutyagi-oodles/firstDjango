from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class AuthToken(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Token for {self.user.username} - {self.token}"