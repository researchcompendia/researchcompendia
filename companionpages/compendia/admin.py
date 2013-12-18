from django.contrib import admin
from .models import Contributor, Article, TaggedArticle
from . import choices


def make_active(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as active"


def make_draft(modeladmin, request, queryset):
    queryset.update(status=choices.STATUS.active)
make_active.short_description = "Mark selected item as draft"


def make_taxonomic(modeladmin, request, queryset):
    queryset.update(tag_type=choices.TAG_TYPES.taxonomic)
make_taxonomic.short_description = "Mark selected tag as taxonomic"


def make_folksonomic(modeladmin, request, queryset):
    queryset.update(tag_type=choices.TAG_TYPES.folksonomic)
make_taxonomic.short_description = "Mark selected tag as folksonomic"


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


class TaggedArticleAdmin(admin.ModelAdmin):
    list_filter = ['tag_type']
    actions = [make_taxonomic, make_folksonomic]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(TaggedArticle, TaggedArticleAdmin)
