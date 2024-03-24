from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'updated']
    search_fields = ['title']
    list_filter = ['title']
