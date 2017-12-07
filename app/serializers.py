from rest_framework.serializers import ModelSerializer

from app.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)