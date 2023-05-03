from django.contrib import admin
from .models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('location', 'created_on')
    list_display = ('title', 'slug', 'trainer', 'location')
    search_fields = ['title', 'trainer__username', 'location']
