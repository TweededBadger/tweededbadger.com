# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.thumbnail'
        db.delete_column(u'blog_image', 'thumbnail')


        # Changing field 'Image.image'
        db.alter_column(u'blog_image', 'image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100))

    def backwards(self, orm):
        # Adding field 'Image.thumbnail'
        db.add_column(u'blog_image', 'thumbnail',
                      self.gf('imagekit.models.fields.ProcessedImageField')(default='', max_length=100),
                      keep_default=False)


        # Changing field 'Image.image'
        db.alter_column(u'blog_image', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'blog.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']