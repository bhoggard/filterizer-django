from django.core.management.base import BaseCommand, CommandError
from artcalendar.models import Event
import os
from buffpy.api import API
from buffpy.managers.profiles import Profiles


class Command(BaseCommand):
    help = "Send today's openings to https://bufferapp.com/"

    def handle(self, *args, **options):
        CLIENT_ID = os.environ.get('BUFFER_CLIENT_ID')
        CLIENT_SECRET = os.environ.get('BUFFER_CLIENT_SECRET')
        ACCESS_TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN')

        api = API(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN)
        profile = Profiles(api=api).filter(service='twitter')[0]

        for event in Event.for_tweeting_today():
            profile.updates.new(event.tweet_text(), shorten=True)
            event.mark_tweeted()

