from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    day = models.DateField(u'Day of event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    location = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
