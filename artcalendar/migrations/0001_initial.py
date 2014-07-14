# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Neighborhood'
        db.create_table(u'artcalendar_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'artcalendar', ['Neighborhood'])

        # Adding model 'Venue'
        db.create_table(u'artcalendar_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artcalendar.Neighborhood'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'artcalendar', ['Venue'])

        # Adding model 'Event'
        db.create_table(u'artcalendar_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artcalendar.Venue'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('opening_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('opening_start_time', self.gf('django.db.models.fields.TimeField')(default='18:00:00', null=True)),
            ('opening_end_time', self.gf('django.db.models.fields.TimeField')(default='20:00:00', null=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('tweeted', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'artcalendar', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Neighborhood'
        db.delete_table(u'artcalendar_neighborhood')

        # Deleting model 'Venue'
        db.delete_table(u'artcalendar_venue')

        # Deleting model 'Event'
        db.delete_table(u'artcalendar_event')


    models = {
        u'artcalendar.event': {
            'Meta': {'ordering': "('-end_date',)", 'object_name': 'Event'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'opening_end_time': ('django.db.models.fields.TimeField', [], {'default': "'20:00:00'", 'null': 'True'}),
            'opening_start_time': ('django.db.models.fields.TimeField', [], {'default': "'18:00:00'", 'null': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tweeted': ('django.db.models.fields.BooleanField', [], {}),
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