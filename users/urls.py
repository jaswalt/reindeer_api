from django.conf.urls import url, include
from .views import UsersView, UserView, check_username, search_name, befriend_user

urlpatterns = [
    url(r'^$', UsersView.as_view()),
    url(r'^checkname$', check_username),
    url(r'^search/(\w+)$', search_name),
    url(r'^([0-9]+)$', UserView.as_view()),
    url(r'^([0-9]+)/befriend/([0-9]+)$', befriend_user),
    url(r'^([0-9]+)/gifts/', include('gifts.urls'))
]
