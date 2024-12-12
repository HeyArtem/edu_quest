from django.contrib import admin

from models_app.models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    # Подписи в шапке
    list_display = [
        "id",
        "test",
        "user",
    ]

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "test",
        "user",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "test",
    ]

    # Справа Фильтр
    list_filter = [
        "test",
    ]

    # Сортирока порядок
    ordering = [
        "test",
        "id",
    ]

    # Пагинация
    list_per_page = 25
