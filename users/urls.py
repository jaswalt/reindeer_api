from django.conf.urls import url, include
from .views import UsersView, UserView, check_username, search_name

urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^checkname$', check_username),
    url(r'^search/(\w+)$', search_name),
    url(r'^([0-9]+)$', UserView.as_view()),
    url(r'^([0-9]+)/gifts/', include('gifts.urls'))
]
