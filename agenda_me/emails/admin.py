from django.contrib import admin

from .models import Email

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('address', 'company')
    list_display_links = ('address', 'company')
    list_filter = ('company',)