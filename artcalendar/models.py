from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)

class Venue(models.Model):
    neighborhood = models.ForeignKey(Neighborhood)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField()
    twitter = models.CharField(max_length=30)
    updated_at = models.DateField(auto_now=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    venue = models.ForeignKey(Venue)
    start_date = models.DateField()
    end_date = models.DateField()
    opening_date = models.DateField(blank=True)
    opening_start_time = models.TimeField(blank=True)
    opening_end_time = models.TimeField(blank=True)
    website = models.URLField()
    tweeted = models.BooleanField()
    updated_at = models.DateField(auto_now=True)
