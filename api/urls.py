"""Define the URL patterns for the API"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from editor.views import ImageListView, ImageView

helper_patterns = [
    # Return a list with images
    url(r'^images/$', ImageListView.as_view(), name='images'),
    url(r'^images/(?P<image_id>\d+)/$', ImageView.as_view(), name='image')
]

urlpatterns = helper_patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
