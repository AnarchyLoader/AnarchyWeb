from django.contrib import admin
from unfold.admin import ModelAdmin

from AnarchyWeb.models import Hack


class HackAdmin(ModelAdmin):
    list_display = [
        "name",
        "description",
        "author",
        "status",
        "process",
        "file",
        "source",
        "game",
        "working",
    ]


admin.site.register(Hack, HackAdmin)
