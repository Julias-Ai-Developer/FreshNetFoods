from django.db import models
from django.contrib.auth.models import User

class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any client-specific fields here, e.g.:
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
