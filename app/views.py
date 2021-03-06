from time import time

from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from app.models import Category, Transaction, Course
from app.paginations import StandardPagination
from app.serializers import CategorySerializer, TransactionSerializer, CourseSerializer


class CategoriesAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardPagination
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        data['user'] = request.user.id
        serializer = CategorySerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)

class CategoryAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionsAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = StandardPagination
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        data['user'] = request.user.id
        data['date'] = int(round(time()))
        serializer = TransactionSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)

class CoursesAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardPagination