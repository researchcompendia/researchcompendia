from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['newsbrief']}),
            ('Publication Date', {'fields': ['publication_date']}),
    ]
    list_display = ('newsbrief', 'publication_date', 'published')
    list_filter = ['publication_date']
    date_heirarchy = ['publication_date']

admin.site.register(News, NewsAdmin)
