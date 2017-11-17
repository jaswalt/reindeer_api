from django.conf.urls import url

from .views import GiftsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', csrf_exempt(GiftsView.as_view())),
]
