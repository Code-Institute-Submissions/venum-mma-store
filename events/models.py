from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    day = models.DateField(u'Day of event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    location = models.CharField(max_length=200)
    notes = models.TextField(u'Textual Notes', help_text=u'Textaul Notes',
                             blank=True, null=True)

    def __str__(self):
        return self.name
