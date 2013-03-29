# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.github_username'
        db.add_column(u'blog_author', 'github_username',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Author.twitter_username'
        db.add_column(u'blog_author', 'twitter_username',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Author.blog_url'
        db.add_column(u'blog_author', 'blog_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Author.github_username'
        db.delete_column(u'blog_author', 'github_username')

        # Deleting field 'Author.twitter_username'
        db.delete_column(u'blog_author', 'twitter_username')

        # Deleting field 'Author.blog_url'
        db.delete_column(u'blog_author', 'blog_url')

    models = {
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
            'blog_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'Post'},
            '_content_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Author']", 'null': 'True', 'blank': 'True'}),
            'content': ('markitup.fields.MarkupField', [], {'no_rendered_field': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']