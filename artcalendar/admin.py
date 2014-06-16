from django.contrib import admin

# Register your models here.
from artcalendar.models import Neighborhood, Venue, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'start_date', 'end_date')
    search_fields = ['title']

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name',)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'neighborhood', 'address', 'twitter')
    search_fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)



