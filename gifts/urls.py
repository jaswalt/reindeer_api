from django.conf.urls import url

from .views import GiftsView, search, getUserWishlists, getWishlistGifts, deleteWishlistGift, postSearchGiftToGifts
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^(\d+)?$', csrf_exempt(GiftsView.as_view())),
    url(r'^wishlists/(\d+)/gifts/(\d+)$', deleteWishlistGift),
    url(r'^wishlists/(\d+)$', getWishlistGifts),
    url(r'^wishlists/$', getUserWishlists),
    url(r'^add/', postSearchGiftToGifts),
    url(r'^search/(\w+)$', search),
]
