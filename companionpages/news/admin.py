from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['newsbrief']}),
        ('Publication Date', {'fields': ['publication_date']}),
    ]
    list_display = ('truncated_newsbrief', 'publication_date', 'published')
    list_filter = ['publication_date']
    date_heirarchy = ['publication_date']

    def truncated_newsbrief(self, news):
        return news.newsbrief[:40]
    truncated_newsbrief.short_description = 'Excerpt'


admin.site.register(News, NewsAdmin)
