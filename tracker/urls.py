from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tracker.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'daas/', include('daas.urls')),
                  url(r'rss/', include('rss.urls')),
                  url(r'app/', include('app.urls')),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
