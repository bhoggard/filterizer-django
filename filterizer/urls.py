from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from artcalendar.models import Neighborhood

from django.contrib import admin
admin.autodiscover()

class NeighborhoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'name',)

class NeighborhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

router = routers.DefaultRouter()
router.register(r'neighborhoods', NeighborhoodViewSet)

urlpatterns = patterns('',
    url(r'^$', 'artcalendar.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
   (r'^selectable/', include('selectable.urls')),

   url(r'^api/', include(router.urls)),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
