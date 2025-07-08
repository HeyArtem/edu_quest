from django.urls import path

from api.views.category import CategoryListCreateAPIView, CategoryTestListAPIView

# Нэйминг маршрутов Объект _ Список или Объект или Детальный просмотр _ Удаление _ APIView
# List - сПисок (GET)
# Retrieve - один объект (GET)
# Create - (POST)
# Update - (PUT/PATCH)
# Delete - (DELETE)

urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("categories/<int:id>/tests/", CategoryTestListAPIView.as_view()),
]
