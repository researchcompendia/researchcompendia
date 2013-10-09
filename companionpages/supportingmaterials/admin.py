from django.contrib import admin
from .models import Collaborator, SupportingMaterial, Article


class SupportingInline(admin.StackedInline):
    model = SupportingMaterial


class CollaboratorInline(admin.StackedInline):
    model = Collaborator


class ArticleAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    inlines = [SupportingInline]


class CollaboratorAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']


class SupportingMaterialAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(SupportingMaterial, SupportingMaterialAdmin)
