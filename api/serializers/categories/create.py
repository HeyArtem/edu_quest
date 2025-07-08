from rest_framework import serializers

from models_app.models import Category


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
        ]
