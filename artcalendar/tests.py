from django.test import TestCase
from artcalendar.models import Venue, Event
# from django.utils import timezone
import datetime

# Create your tests here.
class EventTest(TestCase):
    fixtures = ['neighborhoods.yaml', 'venues.yaml']

    def test_opening_soon(self):
        venue = Venue.objects.get(pk=1)
        today = datetime.datetime.now().date()
        event = Event(venue=venue, title='Matthew Craven', start_date=today,
                      end_date=today + datetime.timedelta(days=30),
                      opening_date=today + datetime.timedelta(days=2))
        event.save()
        event2 = Event(venue=venue, title='Nancy S. Baker', start_date=today,
                       end_date=today + datetime.timedelta(days=30),
                       opening_date=today - datetime.timedelta(days=1))
        event2.save()
        openings = Event.opening_soon()
        self.assertEqual(openings[0], event)

    def test_for_tweeting_today(self):
        venue = Venue.objects.get(pk=1)
        today = datetime.datetime.now().date()
        event = Event(venue=venue, title='Matthew Craven', start_date=today,
                      end_date=today + datetime.timedelta(days=30),
                      opening_date=today)
        event.save()
        event2 = Event(venue=venue, title='Nancy S. Baker', start_date=today,
                       end_date=today + datetime.timedelta(days=30),
                       opening_date=today - datetime.timedelta(days=1))
        event2.save()
        event2.save()
        to_tweet = Event.for_tweeting_today()
        self.assertEqual(to_tweet[0], event)

        self.assertEqual("At DCKT Contemporary @DCKT: Matthew Craven http://www.dcktcontemporary.com/",
            event.tweet_text())

        event.venue.twitter = ''
        self.assertEqual("At DCKT Contemporary: Matthew Craven http://www.dcktcontemporary.com/",
            event.tweet_text())

        event.title = "long stuff " * 15
        event.venue.twitter = 'DCKT'
        self.assertEqual("At DCKT Contemporary @DCKT: long stuff long stuff long stuff long stuff long stuff long stuff long stuff long stuff long... http://www.dcktcontemporary.com/",
            event.tweet_text())

        event.mark_tweeted()
        self.assertTrue(event.tweeted)

    def test_open_now(self):
        venue = Venue.objects.get(pk=1)
        today = datetime.datetime.now().date()
        event = Event(venue=venue, title='Matthew Craven', start_date=today,
                      end_date=today + datetime.timedelta(days=30),
                      opening_date=today)
        event.save()
        hood_list = Event.open_now()
        self.assertEqual(hood_list[0][0], venue.neighborhood.name)
        self.assertEqual(hood_list[0][1], [event])

