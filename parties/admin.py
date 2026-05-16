# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Party


admin.site.site_header = "Контроль партий";
admin.site.site_title = "Контроль партий";

class PartyAdmin(admin.ModelAdmin):
    list_display = ["platform_number",
                    "status",
                    "report_party_file"]
admin.site.register(Party, PartyAdmin)

