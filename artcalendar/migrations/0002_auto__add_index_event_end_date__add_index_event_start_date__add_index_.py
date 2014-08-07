# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Event', fields ['end_date']
        db.create_index(u'artcalendar_event', ['end_date'])

        # Adding index on 'Event', fields ['start_date']
        db.create_index(u'artcalendar_event', ['start_date'])

        # Adding index on 'Event', fields ['opening_date']
        db.create_index(u'artcalendar_event', ['opening_date'])

        # Adding index on 'Event', fields ['tweeted']
        db.create_index(u'artcalendar_event', ['tweeted'])


    def backwards(self, orm):
        # Removing index on 'Event', fields ['tweeted']
        db.delete_index(u'artcalendar_event', ['tweeted'])

        # Removing index on 'Event', fields ['opening_date']
        db.delete_index(u'artcalendar_event', ['opening_date'])

        # Removing index on 'Event', fields ['start_date']
        db.delete_index(u'artcalendar_event', ['start_date'])

        # Removing index on 'Event', fields ['end_date']
        db.delete_index(u'artcalendar_event', ['end_date'])


    models = {
        u'artcalendar.event': {
            'Meta': {'ordering': "('-end_date',)", 'object_name': 'Event'},
            'end_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_index': 'True'}),
            'opening_end_time': ('django.db.models.fields.TimeField', [], {'default': "'20:00:00'", 'null': 'True'}),
            'opening_start_time': ('django.db.models.fields.TimeField', [], {'default': "'18:00:00'", 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tweeted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artcalendar.Venue']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'artcalendar.neighborhood': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Neighborhood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'artcalendar.venue': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artcalendar.Neighborhood']"}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['artcalendar']