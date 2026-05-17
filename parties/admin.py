# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Party
from django.utils.html import format_html


admin.site.site_header = "Контроль партий";
admin.site.site_title = "Контроль партий";

class PartyAdmin(admin.ModelAdmin):
    list_display = [
                    "id",
                    "platform_number",
                    "status",
                    "report_party_file_link",
                    "created"
                    ]
    readonly_fields = ['is_emailed']
    exclude = ('is_emailed',)
    
    def report_party_file_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.report_party_file.url, obj.report_party_file)
    
admin.site.register(Party, PartyAdmin)

