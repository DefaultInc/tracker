from django.conf.urls import url

from rss.views import RSSAPIView

urlpatterns = [
    url(r'^$', RSSAPIView.as_view()),
]