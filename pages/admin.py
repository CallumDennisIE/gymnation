from django.contrib import admin
from .models import Session, Review, Membership


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('location', 'created_on')
    list_display = ('title', 'slug', 'trainer', 'location')
    search_fields = ['title', 'trainer__username', 'location']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'session', 'created_on')
    list_filter = ('created_on',)
    search_filter = ('name', 'session__name', 'email', 'body')


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'member_type')
