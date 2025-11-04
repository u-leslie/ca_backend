from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description')
    readonly_fields = ('organizer',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'registered_at', 'cancelled')
    list_filter = ('cancelled', 'registered_at')
    search_fields = ('event__title', 'user__username')
    actions = ['cancel_selected']

    def cancel_selected(self, request, queryset):
        queryset.update(cancelled=True)
    cancel_selected.short_description = "Cancel selected registrations"