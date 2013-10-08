# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CompanionArticle'
        db.delete_table(u'supportingmaterials_companionarticle')

        # Removing M2M table for field collaborators on 'CompanionArticle'
        db.delete_table(db.shorten_name(u'supportingmaterials_companionarticle_collaborators'))

        # Adding model 'Article'
        db.create_table(u'supportingmaterials_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('status', self.gf('model_utils.fields.StatusField')(default='inactive', max_length=100, no_check_for_status=True)),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status')),
            ('site_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('abstract', self.gf('django.db.models.fields.TextField')(max_length=5000)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('article_url', self.gf('django.db.models.fields.URLField')(max_length=2000, blank=True)),
            ('storage_url', self.gf('django.db.models.fields.URLField')(max_length=2000, blank=True)),
            ('legacy_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('doi', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('primary_research_field', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('secondary_research_field', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'supportingmaterials', ['Article'])

        # Adding M2M table for field collaborators on 'Article'
        m2m_table_name = db.shorten_name(u'supportingmaterials_article_collaborators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm[u'supportingmaterials.article'], null=False)),
            ('collaborator', models.ForeignKey(orm[u'supportingmaterials.collaborator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['article_id', 'collaborator_id'])

        # Deleting field 'SupportingMaterial.companion_article'
        db.delete_column(u'supportingmaterials_supportingmaterial', 'companion_article_id')

        # Adding field 'SupportingMaterial.article'
        db.add_column(u'supportingmaterials_supportingmaterial', 'article',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['supportingmaterials.Article'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'SupportingMaterial.storage_url'
        db.add_column(u'supportingmaterials_supportingmaterial', 'storage_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=2000, blank=True),
                      keep_default=False)


        # Changing field 'SupportingMaterial.materials_url'
        db.alter_column(u'supportingmaterials_supportingmaterial', 'materials_url', self.gf('django.db.models.fields.URLField')(max_length=2000))
        # Deleting field 'Collaborator.member'
        db.delete_column(u'supportingmaterials_collaborator', 'member_id')

        # Adding field 'Collaborator.author_order'
        db.add_column(u'supportingmaterials_collaborator', 'author_order',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field member on 'Collaborator'
        m2m_table_name = db.shorten_name(u'supportingmaterials_collaborator_member')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('collaborator', models.ForeignKey(orm[u'supportingmaterials.collaborator'], null=False)),
            ('member', models.ForeignKey(orm[u'members.member'], null=False))
        ))
        db.create_unique(m2m_table_name, ['collaborator_id', 'member_id'])


    def backwards(self, orm):
        # Adding model 'CompanionArticle'
        db.create_table(u'supportingmaterials_companionarticle', (
            ('status', self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('site_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'], null=True, blank=True)),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status')),
            ('article_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('legacy_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('document', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('abstract', self.gf('django.db.models.fields.TextField')(max_length=5000)),
        ))
        db.send_create_signal(u'supportingmaterials', ['CompanionArticle'])

        # Adding M2M table for field collaborators on 'CompanionArticle'
        m2m_table_name = db.shorten_name(u'supportingmaterials_companionarticle_collaborators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('companionarticle', models.ForeignKey(orm[u'supportingmaterials.companionarticle'], null=False)),
            ('collaborator', models.ForeignKey(orm[u'supportingmaterials.collaborator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['companionarticle_id', 'collaborator_id'])

        # Deleting model 'Article'
        db.delete_table(u'supportingmaterials_article')

        # Removing M2M table for field collaborators on 'Article'
        db.delete_table(db.shorten_name(u'supportingmaterials_article_collaborators'))

        # Adding field 'SupportingMaterial.companion_article'
        db.add_column(u'supportingmaterials_supportingmaterial', 'companion_article',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['supportingmaterials.CompanionArticle']),
                      keep_default=False)

        # Deleting field 'SupportingMaterial.article'
        db.delete_column(u'supportingmaterials_supportingmaterial', 'article_id')

        # Deleting field 'SupportingMaterial.storage_url'
        db.delete_column(u'supportingmaterials_supportingmaterial', 'storage_url')


        # Changing field 'SupportingMaterial.materials_url'
        db.alter_column(u'supportingmaterials_supportingmaterial', 'materials_url', self.gf('django.db.models.fields.URLField')(max_length=200))
        # Adding field 'Collaborator.member'
        db.add_column(u'supportingmaterials_collaborator', 'member',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Collaborator.author_order'
        db.delete_column(u'supportingmaterials_collaborator', 'author_order')

        # Removing M2M table for field member on 'Collaborator'
        db.delete_table(db.shorten_name(u'supportingmaterials_collaborator_member'))


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'biography': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'gravatar_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'public_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'supportingmaterials.article': {
            'Meta': {'ordering': "['title']", 'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['supportingmaterials.Collaborator']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'primary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'secondary_research_field': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']", 'null': 'True', 'blank': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'inactive'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'storage_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'supportingmaterials.collaborator': {
            'Meta': {'ordering': "['author_order', 'name']", 'object_name': 'Collaborator'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'author': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['members.Member']", 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'supportingmaterials.supportingmaterial': {
            'Meta': {'object_name': 'SupportingMaterial'},
            'archive_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['supportingmaterials.Article']", 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'explanatory_text': ('django.db.models.fields.TextField', [], {'max_length': '5000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'inactive'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'storage_url': ('django.db.models.fields.URLField', [], {'max_length': '2000', 'blank': 'True'})
        }
    }

    complete_apps = ['supportingmaterials']