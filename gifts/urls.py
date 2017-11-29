from django.conf.urls import url
from .views import GiftsView, search, createWishlist, getUserWishlists, getWishlistGifts, addWishlistGift, deleteWishlistGift, postSearchGiftToGifts, GiftHoldingsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^(\d+)?$', GiftsView.as_view()),
    url(r'^(\d+)/hold/$', GiftHoldingsView.as_view()),
    url(r'^wishlists/(\d+)/gifts/(\d+)$', deleteWishlistGift),
    url(r'^wishlists/(\d+)/gifts/add$', addWishlistGift),
    url(r'^wishlists/(\d+)$', getWishlistGifts),
    url(r'^wishlists/create$', createWishlist),
    url(r'^wishlists/$', getUserWishlists),
    url(r'^add/', postSearchGiftToGifts),
    url(r'^search/(\w+)$', search),
]
