from django.conf.urls import url

from .views import LiveFeed, LiveDetect, MobileLiveFeed

app_name = "LIVE"

urlpatterns = [
    url('detect/', LiveDetect.as_view(), name='detect'),
    url('livefeed/',LiveFeed.as_view(), name='feed'),
    url('mobilefeed/', MobileLiveFeed.as_view(),name='mobile')
]