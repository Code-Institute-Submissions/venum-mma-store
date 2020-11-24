from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    """Create the contact model."""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    from_email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
