from django.contrib import admin
from django import forms
import selectable.forms as selectable
from artcalendar.lookups import VenueLookup
from artcalendar.models import Neighborhood, Venue, Event

class EventAdminForm(forms.ModelForm):
    venue = selectable.AutoCompleteSelectField(lookup_class=VenueLookup, allow_new=False)

    class Meta(object):
        model = Event
        exclude = ('venue', )

    def __init__(self, *args, **kwargs):
        super(EventAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.owner:
            self.initial['venue'] = self.instance.venue.pk

    def save(self, *args, **kwargs):
        venue = self.cleaned_data['venue']
        self.instance.venue = venue
        return super(EventAdminForm, self).save(*args, **kwargs)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'start_date', 'end_date')
    search_fields = ['title']
    form = EventAdminForm

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name',)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'neighborhood', 'address', 'twitter')
    search_fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)

