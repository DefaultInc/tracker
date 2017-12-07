from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from daas.views import RegisterAPIView, ProfileAPIView

urlpatterns = [
    url(r'^register/$', RegisterAPIView.as_view()),
    url(r'^login/$', obtain_jwt_token),
    url(r'^profile/$', ProfileAPIView.as_view()),
]
