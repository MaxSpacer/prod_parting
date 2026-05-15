# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Party


admin.site.site_header = "Контроль партий";
admin.site.site_title = "Контроль партий";

class PartyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Party._meta.fields]
admin.site.register(Party, PartyAdmin)

