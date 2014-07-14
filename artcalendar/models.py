from django.db import models
from django.utils import timezone
import datetime

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Venue(models.Model):
    neighborhood = models.ForeignKey(Neighborhood)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField()
    twitter = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Event(models.Model):
    title = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)
    start_date = models.DateField()
    end_date = models.DateField()
    opening_date = models.DateField(null=True)
    opening_start_time = models.TimeField(null=True, default='18:00:00')
    opening_end_time = models.TimeField(null=True, default='20:00:00')
    website = models.URLField(blank=True)
    tweeted = models.BooleanField()

    def __unicode__(self):
        return self.title
        # return "%s (%s)" % self.title, self.venue.name

    class Meta:
        ordering = ('-end_date',)

    @classmethod
    def opening_soon(cls):
        return cls.objects.filter(opening_date__gte=timezone.now(),
                       opening_date__lte=timezone.now() + datetime.timedelta(days=10)
                      ).order_by('opening_date', 'opening_start_time')
