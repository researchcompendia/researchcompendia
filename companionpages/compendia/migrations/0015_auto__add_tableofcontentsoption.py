# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TableOfContentsOption'
        db.create_table(u'compendia_tableofcontentsoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compendium_type', self.gf('django.db.models.fields.CharField')(default='misc', unique=True, max_length=100)),
            ('description', self.gf('markitup.fields.MarkupField')(max_length=500, no_rendered_field=True, blank=True)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'compendia', ['TableOfContentsOption'])


    def backwards(self, orm):
        # Deleting model 'TableOfContentsOption'
        db.delete_table(u'compendia_tableofcontentsoption')


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
            '_admin_notes_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_code_data_abstract_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_manual_citation_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_paper_abstract_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'admin_notes': ('markitup.fields.MarkupField', [], {'max_length': '5000', 'no_rendered_field': 'True', 'blank': 'True'}),
            'article_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'authors_text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'authorship': ('jsonfield.fields.JSONField', [], {'default': "'{}'"}),
            'bibjson': ('jsonfield.fields.JSONField', [], {'default': "'{}'"}),
            'book_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'code_data_abstract': ('markitup.fields.MarkupField', [], {'max_length': '5000', 'no_rendered_field': 'True', 'blank': 'True'}),
            'code_doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'code_license': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'compendium_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content_license': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'contributors'", 'to': u"orm['users.User']", 'through': u"orm['compendia.Contributor']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'data_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'data_doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'homework_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lecture_notes_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'manual_citation': ('markitup.fields.MarkupField', [], {'max_length': '500', 'no_rendered_field': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'notes_for_staff': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'paper_abstract': ('markitup.fields.MarkupField', [], {'max_length': '5000', 'no_rendered_field': 'True', 'blank': 'True'}),
            'primary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'related_urls': ('jsonfield.fields.JSONField', [], {'default': "'{}'"}),
            'secondary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'solution_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'verification_archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'compendia.tableofcontentsoption': {
            'Meta': {'object_name': 'TableOfContentsOption'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'compendium_type': ('django.db.models.fields.CharField', [], {'default': "'misc'", 'unique': 'True', 'max_length': '100'}),
            'description': ('markitup.fields.MarkupField', [], {'max_length': '500', 'no_rendered_field': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'compendia.taggedarticle': {
            'Meta': {'object_name': 'TaggedArticle'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'compendia_taggedarticle_items'", 'to': u"orm['taggit.Tag']"}),
            'tag_type': ('django.db.models.fields.CharField', [], {'default': "'folksonomic'", 'max_length': '50', 'blank': 'True'})
        },
        u'compendia.verification': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Verification'},
            'archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'archive_info': ('jsonfield.fields.JSONField', [], {'default': "'{}'"}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['compendia.Article']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parameters': ('jsonfield.fields.JSONField', [], {'default': "'{}'"}),
            'requestid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('article',)", 'max_length': '50', 'populate_from': "'populate_slug'"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'unknown'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'stderr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stdout': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
            'urls': ('json_field.fields.JSONField', [], {'default': "'{}'"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['compendia']