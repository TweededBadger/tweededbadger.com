# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Post.description'
        db.alter_column(u'blog_post', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Post.external_data'
        db.alter_column(u'blog_post', 'external_data', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Post.content'
        db.alter_column(u'blog_post', 'content', self.gf('tinymce.models.HTMLField')(null=True))

    def backwards(self, orm):

        # Changing field 'Post.description'
        db.alter_column(u'blog_post', 'description', self.gf('django.db.models.fields.CharField')(default=1, max_length=255))

        # Changing field 'Post.external_data'
        db.alter_column(u'blog_post', 'external_data', self.gf('django.db.models.fields.TextField')(default=1))

        # Changing field 'Post.content'
        db.alter_column(u'blog_post', 'content', self.gf('tinymce.models.HTMLField')(default=1))

    models = {
        u'blog.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'external_data': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.PostType']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'thumbnail': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['blog']