from django.contrib import admin

from models_app.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Подписи в шапке
    list_display = [
        "id",
        "title",
    ]

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "title",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "title",
    ]

    # Сортирока порядок
    ordering = [
        "title",
    ]

    # Пагинация
    list_per_page = 25
