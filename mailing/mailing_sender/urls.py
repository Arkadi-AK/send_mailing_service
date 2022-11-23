from django.conf.urls import url

from mailing_sender.views import PixelView

urlpatterns = [
    url(r"^open-tracking/(?P<client>[0-9]+)/$", PixelView.as_view(), name="pixel_view"),
]
