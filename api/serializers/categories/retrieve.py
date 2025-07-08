from rest_framework import serializers

from models_app.models import Category, Test, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class TestSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Test
        fields = [
            "id",
            "title",
            "created_at",
            "author",
        ]


class RetrieveCategorySerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "tests",  # related_name подтянет все тесты этой категории
        ]
