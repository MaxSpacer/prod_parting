from django.contrib import admin
from .models import Party


# class PartyItemInline(admin.TabularInline):
# 	model = PartyItem
 

class PartyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Party._meta.fields]
    # inlines = [PartyItemInline]
admin.site.register(Party, PartyAdmin)

