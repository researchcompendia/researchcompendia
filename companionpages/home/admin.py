from django.contrib import admin
from .models import Faq

class FaqAdmin(admin.ModelAdmin):
    list_display = ('truncated_question', 'modified')
    list_filter = ['modified']
    date_heirarchy = ['modified']

    def truncated_question(self, faq):
        return faq.question[:40]

admin.site.register(Faq, FaqAdmin)
