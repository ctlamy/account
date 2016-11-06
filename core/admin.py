from django.contrib import admin

from core.models import Entry

class EntryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Entry, EntryAdmin)