# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Faq.index'
        db.add_column(u'home_faq', 'index',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Faq.index'
        db.delete_column(u'home_faq', 'index')


    models = {
        u'home.faq': {
            'Meta': {'ordering': "['index', 'created']", 'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['home']