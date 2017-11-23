"""reindeer_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from gifts import views as gifts
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


urlpatterns = [
    url(r'^$', gifts.index),
    url(r'^api/v1/', include([
        url(r'^users/', include('users.urls')),
    ])),
    url(r'^api/token/', include([
        url(r'^$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        url(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
        url(r'^verify/$', TokenVerifyView.as_view(), name='token_verify'),
    ])),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
