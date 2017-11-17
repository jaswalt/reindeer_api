from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)$', views.show),
    url(r'^([0-9]+)/gifts/', include('gifts.urls'))
]