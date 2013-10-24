from django.contrib import admin
from .models import Collaborator, SupportingMaterial, Article


def make_active(modeladmin, request, queryset):
    queryset.update(status=Article.STATUS.active)
make_active.short_description = "Mark selected item as active"


class SupportingInline(admin.StackedInline):
    model = SupportingMaterial


class CollaboratorInline(admin.StackedInline):
    model = Collaborator


class ArticleAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['status', 'created']
    inlines = [SupportingInline]
    actions = [make_active]


class CollaboratorAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['created']


class SupportingMaterialAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['status', 'created']
    actions = [make_active]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(SupportingMaterial, SupportingMaterialAdmin)
