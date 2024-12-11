from django.contrib import admin

from models_app.models import UserResult


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = [
        "id",
        "test",
        "user",
        "date",
    ]

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "test",
        "user",
        "date",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "test",
        "user",
    ]

    # Справа Фильтр
    list_filter = [
        "date",
    ]

    # Сортирока порядок
    ordering = [
        "date",
    ]

    # Пагинация
    list_per_page = 20

    # сверху строка навигации по датам
    date_hierarchy = "date"
