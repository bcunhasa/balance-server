"""Define the URLS for the server"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'', include('editor.urls', namespace='editor')),
]
