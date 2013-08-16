from django.contrib import admin
from .models import CompanionArticle, SupportingMaterial

class CompanionArticleAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']

class SupportingMaterialAdmin(admin.ModelAdmin):
    date_heirarchy = ['created']

admin.site.register(CompanionArticle, CompanionArticleAdmin)
admin.site.register(SupportingMaterial, SupportingMaterialAdmin)
