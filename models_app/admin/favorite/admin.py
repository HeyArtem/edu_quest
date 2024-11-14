from django.contrib import admin

from models_app.models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    # list_display = ('id', 'User', 'test',)
    list_display = (
        "id",
        "test",
    )

    # Кликабельность в шапке
    list_display_links = (
        "id",
        "test",
    )

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ("test",)

    # Справа Фильтр
    list_filter = (
        "id",
        "test",
    )

    # Сортирока порядок
    ordering = (
        "test",
        "id",
    )

    # Пагинация
    list_per_page = 10
