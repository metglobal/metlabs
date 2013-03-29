# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'blog_author', (
            (u'id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name',
             self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image',
             self.gf('django.db.models.fields.files.ImageField')(max_length=100,
                                                                 null=True,
                                                                 blank=True)),
        ))
        db.send_create_signal(u'blog', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'blog_author')


    models = {
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
            'full_name': (
                'django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': (
                'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [],
                      {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "('-date_created',)", 'object_name': 'Post'},
            '_content_rendered': (
                'django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': (
                'markitup.fields.MarkupField', [], {'no_rendered_field': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [],
                             {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [],
                              {'auto_now': 'True', 'auto_now_add': 'True',
                               'blank': 'True'}),
            u'id': (
                'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': (
                'django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [],
                     {'unique': 'True', 'max_length': '255'}),
            'title': (
                'django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']