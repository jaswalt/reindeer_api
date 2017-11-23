from django.conf.urls import url, include

from .views import UsersView, UserView

urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^([0-9]+)$', UserView.as_view()),
    url(r'^([0-9]+)/gifts/', include('gifts.urls'))
]
