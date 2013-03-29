# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Session.description'
        db.add_column(u'events_session', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Session.content'
        db.add_column(u'events_session', 'content',
                      self.gf('markitup.fields.MarkupField')(blank=True, null=True, no_rendered_field=True),
                      keep_default=False)

        # Adding field 'Session._content_rendered'
        db.add_column(u'events_session', '_content_rendered',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Session.description'
        db.delete_column(u'events_session', 'description')

        # Deleting field 'Session.content'
        db.delete_column(u'events_session', 'content')

        # Deleting field 'Session._content_rendered'
        db.delete_column(u'events_session', '_content_rendered')

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
            '_content_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('markitup.fields.MarkupField', [], {'blank': 'True', 'null': 'True', 'no_rendered_field': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessions'", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']