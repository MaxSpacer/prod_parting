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
                    "report_party",
                    "view_csv",
                    "download_xls",
                    "created"
                    ]
    
    readonly_fields = ['is_emailed', 'report_party_file']
    exclude = ('is_emailed',)
    
    def report_party(self, obj):
        return format_html('<a href="{}" target="_blank" rel="noopener noreferrer"  target="_blank" class="button">{}</a>', obj.report_party_file.url, 'Cкачать CSV')
    
    def view_csv(self, obj):
        return format_html('<a href="/admin/read_csv_file/{}" rel="noopener noreferrer"  target="_blank" class="button">Просмотр</a>', obj.id)
    
    def download_xls(self, obj):
        return format_html('<a href="/admin/create_xls/{}" rel="noopener noreferrer"  target="_blank" class="button">Скачать XLS</a>', obj.id)
    
    
    # <input type="submit" value="Сохранить" class="default" name="_save">
    
    
    
    
admin.site.register(Party, PartyAdmin)

