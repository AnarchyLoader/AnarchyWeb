from django.contrib import admin

from AnarchyWeb.models import Hack


class HackAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'author', 'status', 'process', 'file', 'source', 'game']

admin.site.register(Hack, HackAdmin)