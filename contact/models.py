from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):
    """Create the contact model. create foreign key to the user table.
    This will allow the superuser to see what user
    made an enquiry if they are logged in."""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_subject = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_body = models.TextField(max_length=5000)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    query_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_subject
