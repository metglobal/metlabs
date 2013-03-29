# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attendee'
        db.create_table(u'events_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'events', ['Attendee'])

        # Adding unique constraint on 'Attendee', fields ['event', 'email']
        db.create_unique(u'events_attendee', ['event_id', 'email'])

        # Removing M2M table for field attendees on 'Event'
        db.delete_table('events_event_attendees')

    def backwards(self, orm):
        # Removing unique constraint on 'Attendee', fields ['event', 'email']
        db.delete_unique(u'events_attendee', ['event_id', 'email'])

        # Deleting model 'Attendee'
        db.delete_table(u'events_attendee')

        # Adding M2M table for field attendees on 'Event'
        db.create_table(u'events_event_attendees', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'events_event_attendees', ['event_id', 'user_id'])

    models = {
        u'events.attendee': {
            'Meta': {'unique_together': "(('event', 'email'),)", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('markitup.fields.MarkupField', [], {'blank': 'True', 'null': 'True', 'no_rendered_field': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']