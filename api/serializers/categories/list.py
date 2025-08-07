from rest_framework import serializers

from models_app.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор.
    ModelSerializer-удобен, что сам определяет типы данных
        (DateTimeField, CharField, BooleanField и др.)
    Использую для:
        -Чтения и фильтрации на APIView & ListAPIView (generics)
        -Создания на APIView & ListAPIView (generics)
    """

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ["id", "title"]
