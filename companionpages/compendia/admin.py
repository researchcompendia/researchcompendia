from django.contrib import admin
from .models import Contributor, Article
from . import choices


def make_active(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as active"


def make_draft(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as draft"


class ContributorInline(admin.StackedInline):
    model = Contributor


class ArticleAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['status', 'created', 'compendium_type', 'primary_research_field']
    inlines = [ContributorInline]
    actions = [make_active, make_draft]


class ContributorAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']
    list_filter = ['created', 'role']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor, ContributorAdmin)
