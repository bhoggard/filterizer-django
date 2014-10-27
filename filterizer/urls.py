from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets
from artcalendar.models import Neighborhood
from django.contrib.auth.models import User

from django.contrib import admin
admin.autodiscover()

class NeighborhoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'name',)

class NeighborhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active')

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)

router = routers.DefaultRouter()
router.register(r'neighborhoods', NeighborhoodViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    url(r'^$', 'artcalendar.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^selectable/', include('selectable.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    # browseable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
