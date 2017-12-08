from rest_framework.serializers import ModelSerializer

from app.models import Category, Transaction, Course


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('name', 'price', 'category', 'date',)
    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'price')
    def create(self, validated_data):
        return Course.objects.create(**validated_data)