from django.test import TestCase
from artcalendar.models import Venue, Event
from django.utils import timezone
import datetime

# Create your tests here.
class EventTest(TestCase):
    fixtures = ['neighborhoods.yaml', 'venues.yaml']

    def test_opening_soon(self):
        venue = Venue.objects.get(pk=1)
        event = Event(venue=venue, title='Matthew Craven', start_date=timezone.now(),
                             end_date=timezone.now() + datetime.timedelta(days=30),
                             opening_date=timezone.now() + datetime.timedelta(days=3))
        event.save
        event2 = Event(venue=venue, title='Matthew Craven', start_date=timezone.now(),
                             end_date=timezone.now() + datetime.timedelta(days=30),
                             opening_date=timezone.now() - datetime.timedelta(days=1))
        event2.save
        list = Event.opening_soon()
        self.assertEqual(list, event)