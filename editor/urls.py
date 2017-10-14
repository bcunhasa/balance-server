"""Define the URLS standards for editor"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Inicial page
    url(r'^$', views.index, name='index'),
]
