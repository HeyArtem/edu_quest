from rest_framework import serializers

from models_app.models import Test


class RetrieveCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор.
    ModelSerializer-удобен, что сам определяет типы данных
        (DateTimeField, CharField, BooleanField и др.)
    """

    class Meta:
        model = Test
        fields = ["id", "title", "category"]
