from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('public_name', 'website', 'status', 'created', 'modified')
    date_heirarchy = ['created']

admin.site.register(Member, MemberAdmin)
