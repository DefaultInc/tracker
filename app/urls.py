from django.conf.urls import url
from app.views import CategoriesAPIView, CategoryAPIView, TransactionsAPIView

urlpatterns = [
    url(r'categories/$', CategoriesAPIView.as_view()),
    url(r'categories/(?P<pk>[0-9]+)/$', CategoryAPIView.as_view()),
    url(r'transactions/$', TransactionsAPIView.as_view()),
]
