#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "filterizer.settings")

from django.db import connections
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist
from artcalendar import models

def setup_cursor():
    try:
        cursor = connections['legacy'].cursor()
    except ConnectionDoesNotExist:
        print "Legacy database is not configured"
        return None
    return cursor

def import_neighborhoods():
    cursor = setup_cursor()
    if cursor is None:
        return
    sql = "SELECT id, name FROM neighborhoods"
    cursor.execute(sql)
    for row in cursor.fetchall():
        neighborhood = models.Neighborhood(id=row[0], name=row[1])
        neighborhood.save()

def import_venues():
    cursor = setup_cursor()
    if cursor is None:
        return
    sql = """SELECT id, neighborhood_id, name, address, website, twitter FROM venues"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        try:
            neighborhood = models.Neighborhood.objects.get(id=row[1])
        except ObjectDoesNotExist:
            print "Neighborhood not found with id %s" % row[1]
            continue
        else:
            venue = models.Venue(
                id=row[0],
                neighborhood=neighborhood,
                name=row[2],
                address=row[3],
                website=row[4],
                twitter=(row[5] or ''),
            )
            venue.save()

def import_events():
    cursor = setup_cursor()
    if cursor is None:
        return
    sql = """SELECT id, venue_id, title, start_date, end_date, opening_date,
        opening_start_time, opening_end_time, website, tweeted
        FROM events"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        try:
            venue = models.Venue.objects.get(id=row[1])
        except ObjectDoesNotExist:
            print "Venue not found with id %s" % row[1]
            continue
        else:
            event = models.Event(
                id=row[0],
                venue=venue,
                title=row[2],
                start_date=row[3],
                end_date=row[4],
                website=row[8],
                tweeted=row[9],
            )

            # opening date?
            if row[5]:
                event.opening_date = row[5]
                event.opening_start_time=row[6]
                event.opening_end_time=row[7]

            event.save()

def main():
    import_neighborhoods()
    import_venues()
    import_events()

if __name__=="__main__":
    main()
