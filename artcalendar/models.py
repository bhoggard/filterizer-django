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
    tweeted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
        # return "%s (%s)" % self.title, self.venue.name

    class Meta:
        ordering = ('-end_date',)

    @classmethod
    def opening_soon(cls):
        today = timezone.now().date()
        return cls.objects.filter(opening_date__gte=today,
                       opening_date__lte=today + datetime.timedelta(days=10)
                      ).order_by('opening_date', 'opening_start_time')
    @classmethod
    def for_tweeting_today(cls):
        return cls.objects.filter(
            opening_date=timezone.now().date(),
            tweeted=False
            ).order_by('id')

    @classmethod
    def open_now(cls):
        """Return Events that are open now, organized by Neighborhood"""
        hood_list = []
        today = timezone.now().date()
        for hood in Neighborhood.objects.all().order_by('name'):
            events = Event.objects.filter(
                venue__neighborhood=hood,
                start_date__lte=today,
                end_date__gte=today
                ).order_by('-end_date')
            if len(events) > 0:
                hood_list.append([hood.name, list(events)])
        return hood_list




