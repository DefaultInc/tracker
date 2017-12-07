from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class RSSAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
