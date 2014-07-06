from artcalendar.models import Venue

from selectable.base import ModelLookup
from selectable.registry import registry

class VenueLookup(ModelLookup):
    model = Venue
    search_fields = ('name__icontains', )

registry.register(VenueLookup)