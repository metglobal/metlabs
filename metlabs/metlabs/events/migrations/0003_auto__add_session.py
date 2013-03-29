# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Session'
        db.create_table(u'events_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sessions', to=orm['events.Event'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('speaker', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Session'])

    def backwards(self, orm):
        # Deleting model 'Session'
        db.delete_table(u'events_session')

    models = {
        u'events.attendee': {
            'Meta': {'unique_together': "(('event', 'email'),)", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attendees'", 'to': u"orm['events.Event']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'events.event': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Event'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('markitup.fields.MarkupField', [], {'blank': 'True', 'null': 'True', 'no_rendered_field': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_participants': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'events.session': {
            'Meta': {'object_name': 'Session'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessions'", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']