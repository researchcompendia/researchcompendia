# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.month'
        db.add_column(u'compendia_article', 'month',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.year'
        db.add_column(u'compendia_article', 'year',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.volume'
        db.add_column(u'compendia_article', 'volume',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.number'
        db.add_column(u'compendia_article', 'number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.pages'
        db.add_column(u'compendia_article', 'pages',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Article.manual_citation'
        db.add_column(u'compendia_article', 'manual_citation',
                      self.gf('markitup.fields.MarkupField')(default='', max_length=500, no_rendered_field=True, blank=True),
                      keep_default=False)

        # Adding field 'Article.bibjson'
        db.add_column(u'compendia_article', 'bibjson',
                      self.gf('jsonfield.fields.JSONField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Article._manual_citation_rendered'
        db.add_column(u'compendia_article', '_manual_citation_rendered',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Article.related_urls'
        db.alter_column(u'compendia_article', 'related_urls', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'Article.authorship'
        db.alter_column(u'compendia_article', 'authorship', self.gf('jsonfield.fields.JSONField')())

    def backwards(self, orm):
        # Deleting field 'Article.month'
        db.delete_column(u'compendia_article', 'month')

        # Deleting field 'Article.year'
        db.delete_column(u'compendia_article', 'year')

        # Deleting field 'Article.volume'
        db.delete_column(u'compendia_article', 'volume')

        # Deleting field 'Article.number'
        db.delete_column(u'compendia_article', 'number')

        # Deleting field 'Article.pages'
        db.delete_column(u'compendia_article', 'pages')

        # Deleting field 'Article.manual_citation'
        db.delete_column(u'compendia_article', 'manual_citation')

        # Deleting field 'Article.bibjson'
        db.delete_column(u'compendia_article', 'bibjson')

        # Deleting field 'Article._manual_citation_rendered'
        db.delete_column(u'compendia_article', '_manual_citation_rendered')


        # Changing field 'Article.related_urls'
        db.alter_column(u'compendia_article', 'related_urls', self.gf('json_field.fields.JSONField')())

        # Changing field 'Article.authorship'
        db.alter_column(u'compendia_article', 'authorship', self.gf('json_field.fields.JSONField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'compendia.article': {
            'Meta': {'ordering': "['title']", 'object_name': 'Article'},
            '_code_data_abstract_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_manual_citation_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_paper_abstract_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'article_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'authors_text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'authorship': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'bibjson': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'code_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'code_data_abstract': ('markitup.fields.MarkupField', [], {'max_length': '5000', 'no_rendered_field': 'True', 'blank': 'True'}),
            'code_license': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'compendium_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content_license': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contributors'", 'to': u"orm['users.User']", 'through': u"orm['compendia.Contributor']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'data_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'manual_citation': ('markitup.fields.MarkupField', [], {'max_length': '500', 'no_rendered_field': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'notes_for_staff': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'paper_abstract': ('markitup.fields.MarkupField', [], {'max_length': '5000', 'no_rendered_field': 'True', 'blank': 'True'}),
            'primary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'related_urls': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'secondary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        u'compendia.contributor': {
            'Meta': {'ordering': "['citation_order', 'user']", 'object_name': 'Contributor'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            'citation_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'compendia.taggedarticle': {
            'Meta': {'object_name': 'TaggedArticle'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'compendia_taggedarticle_items'", 'to': u"orm['taggit.Tag']"}),
            'tag_type': ('django.db.models.fields.CharField', [], {'default': "'folksonomic'", 'max_length': '50', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'urls': ('json_field.fields.JSONField', [], {'default': "u'null'", 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['compendia']