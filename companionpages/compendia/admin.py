from django.contrib import admin
from .models import Contributor, SupportingMaterial, Article
from . import choices


def make_active(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as active"


def make_draft(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as draft"


class SupportingInline(admin.StackedInline):
    model = SupportingMaterial


class ContributorInline(admin.StackedInline):
    model = Contributor


class ArticleAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['status', 'created', 'primary_research_field']
    inlines = [ContributorInline, SupportingInline]
    actions = [make_active, make_draft]


class ContributorAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['created', 'role', 'primary']


class SupportingMaterialAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['status', 'created', 'materials_type']
    actions = [make_active, make_draft]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(SupportingMaterial, SupportingMaterialAdmin)
